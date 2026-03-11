// ==========================================
// CONFIGURATION ET ÉLÉMENTS UI
// ==========================================
const ui = {
    chatBox: document.getElementById('chat-box'),
    userInput: document.getElementById('user-input'),
    sendBtn: document.getElementById('send-btn'),
    clearBtn: document.getElementById('clear-btn'),
    imageUpload: document.getElementById('image-upload'),
    imageLabel: document.getElementById('image-upload-label'),
    previewContainer: document.getElementById('image-preview-container'),
    imagePreview: document.getElementById('image-preview'),
    removeImageBtn: document.getElementById('remove-image-btn'),
    chatContainer: document.getElementById('chat-container')
};

const STATE = {
    historyKey: 'mon_chat_prive_historique',
    localHistory: [],
    isRequestPending: false,
    selectedImage: null
};

// ==========================================
// UTILITAIRES ET SÉCURITÉ
// ==========================================
const utils = {
    extractText: (res) => {
        if (!res) return "";
        if (typeof res === 'string') return res;
        if (res.choices?.[0]?.message?.content) return res.choices[0].message.content;
        if (res.message?.content) return res.message.content;
        if (res.text) return res.text;
        try { return JSON.stringify(res); } catch { return "Erreur de lecture."; }
    },
    escapeHTML: (str) => {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    },
    scrollToBottom: () => {
        ui.chatBox.scrollTo({ top: ui.chatBox.scrollHeight, behavior: 'smooth' });
    }
};

// ==========================================
// GESTION DES IMAGES (Sélection & Drag/Drop)
// ==========================================
const imageManager = {
    setImage: (file) => {
        if (!file || !file.type.startsWith('image/')) return;
        STATE.selectedImage = file;
        ui.imageLabel.classList.add('active');
        
        // Afficher l'aperçu
        const reader = new FileReader();
        reader.onload = (e) => {
            ui.imagePreview.src = e.target.result;
            ui.previewContainer.style.display = 'flex';
        };
        reader.readAsDataURL(file);
    },
    clearImage: () => {
        STATE.selectedImage = null;
        ui.imageUpload.value = '';
        ui.imageLabel.classList.remove('active');
        ui.previewContainer.style.display = 'none';
        ui.imagePreview.src = '';
    }
};

// Événements liés à l'image
ui.imageUpload.addEventListener('change', (e) => imageManager.setImage(e.target.files[0]));
ui.removeImageBtn.addEventListener('click', imageManager.clearImage);

// Glisser-Déposer (Drag & Drop)
ui.chatContainer.addEventListener('dragover', (e) => { 
    e.preventDefault(); 
    ui.chatContainer.classList.add('dragover'); 
});
ui.chatContainer.addEventListener('dragleave', () => ui.chatContainer.classList.remove('dragover'));
ui.chatContainer.addEventListener('drop', (e) => {
    e.preventDefault();
    ui.chatContainer.classList.remove('dragover');
    if (e.dataTransfer.files.length) imageManager.setImage(e.dataTransfer.files[0]);
});

// ==========================================
// GESTION DU CHAT ET HISTORIQUE
// ==========================================
const chatManager = {
    addMessage: (htmlContent, type, saveToHistory = true) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${type}`;
        msgDiv.innerHTML = htmlContent;
        ui.chatBox.appendChild(msgDiv);
        utils.scrollToBottom();

        if (saveToHistory && type !== 'system-msg') {
            chatManager.saveMessage(htmlContent, type);
        }
    },
    addSystemStatus: (text) => {
        const statusDiv = document.createElement('div');
        statusDiv.className = 'message system-msg';
        statusDiv.innerHTML = text;
        ui.chatBox.appendChild(statusDiv);
        utils.scrollToBottom();
        return statusDiv;
    },
    loadHistory: async () => {
        try {
            const data = await puter.kv.get(STATE.historyKey);
            if (data) {
                STATE.localHistory = JSON.parse(data);
                STATE.localHistory.forEach(msg => chatManager.addMessage(msg.html, msg.type, false));
            }
        } catch {
            puter.kv.del(STATE.historyKey);
            STATE.localHistory = [];
        }
    },
    saveMessage: async (html, type) => {
        try {
            STATE.localHistory.push({ html, type });
            // Sécurité : On ne garde que les 30 derniers messages pour éviter de faire planter la base de données
            if (STATE.localHistory.length > 30) STATE.localHistory.shift();
            await puter.kv.set(STATE.historyKey, JSON.stringify(STATE.localHistory));
        } catch (e) { console.error("Erreur de sauvegarde", e); }
    },
    clearHistory: async () => {
        if(confirm("Voulez-vous effacer toute la conversation ?")) {
            await puter.kv.del(STATE.historyKey);
            STATE.localHistory = [];
            ui.chatBox.innerHTML = '<div class="system-msg">👋 Historique effacé.</div>';
        }
    },
    getContext: () => {
        // Envoie les 2 derniers textes (sans le code HTML des images) pour la mémoire de l'IA
        const recent = STATE.localHistory.slice(-2).map(msg => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = msg.html;
            const role = msg.type === 'user-msg' ? 'User' : 'IA';
            return `${role}: ${tempDiv.textContent}`;
        }).join('\n');
        return recent ? `Contexte récent:\n${recent}\n\n` : "";
    }
};

// ==========================================
// LOGIQUE MULTI-AGENTS IA (Vitesse Max)
// ==========================================
const aiManager = {
    setLoadingState: (isLoading) => {
        STATE.isRequestPending = isLoading;
        ui.sendBtn.disabled = isLoading;
        ui.userInput.disabled = isLoading;
        ui.imageUpload.disabled = isLoading;
        if (!isLoading) ui.userInput.focus();
    },
    send: async () => {
        if (STATE.isRequestPending) return;
        
        const question = ui.userInput.value.trim();
        const imageFile = STATE.selectedImage;
        
        if (!question && !imageFile) return;

        aiManager.setLoadingState(true);

        // Construction de la bulle utilisateur avec miniature s'il y a une image
        let userHtml = question ? utils.escapeHTML(question).replace(/\n/g, '<br>') : "<i>Image envoyée</i>";
        if (imageFile) {
            userHtml += `<br><img src="${ui.imagePreview.src}" alt="Image jointe">`;
        }
        
        chatManager.addMessage(userHtml, 'user-msg');
        ui.userInput.value = '';
        imageManager.clearImage(); // Nettoyage immédiat de l'UI

        const statusDiv = chatManager.addSystemStatus(imageFile ? "👁️ Analyse visuelle en cours..." : "⚡ Réflexion parallèle...");

        try {
            const ctx = chatManager.getContext();
            const promptBase = question || "Que vois-tu de remarquable ici ?";

            // ÉTAPE 1 : Requêtes simultanées avec puter.js (ultra-rapide grâce aux limites)
            const p1 = puter.ai.chat(`${ctx}Tu es pragmatique. Réponds en 2 phrases MAX à: "${promptBase}"`, imageFile);
            const p2 = puter.ai.chat(`${ctx}Tu es critique. Soulève 1 nuance en 1 phrase MAX sur: "${promptBase}"`, imageFile);

            const [res1, res2] = await Promise.all([p1, p2]);
            const avis1 = utils.extractText(res1);
            const avis2 = utils.extractText(res2);

            statusDiv.innerHTML = "✨ Synthèse finale...";

            // ÉTAPE 2 : Le Juge Final
            const promptFinal = `Tu es l'expert final. Fais la synthèse pour répondre à "${promptBase}". 
            Brouillon pragmatique: "${avis1}". Nuance soulevée: "${avis2}". 
            Réponds directement et proprement, sans salutations.`;

            const finalRes = await puter.ai.chat(promptFinal, imageFile);
            
            // Affichage
            statusDiv.remove();
            const reponseFinaleHtml = utils.escapeHTML(utils.extractText(finalRes)).replace(/\n/g, '<br>');
            chatManager.addMessage(reponseFinaleHtml, 'ai-msg');

        } catch (err) {
            statusDiv.remove();
            chatManager.addSystemStatus("❌ Erreur réseau ou image trop lourde.");
            console.error("Erreur IA:", err);
        } finally {
            aiManager.setLoadingState(false);
        }
    }
};

// ==========================================
// INITIALISATION DES ÉVÉNEMENTS
// ==========================================
ui.sendBtn.addEventListener('click', aiManager.send);
if (ui.clearBtn) ui.clearBtn.addEventListener('click', chatManager.clearHistory);
ui.userInput.addEventListener('keypress', (e) => { 
    if (e.key === 'Enter') aiManager.send(); 
});

// Lancement
chatManager.loadHistory();