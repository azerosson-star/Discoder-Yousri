# 🤖 Configuration de l'IA pour votre Chatbot

Votre chatbot peut maintenant être connecté à des IA puissantes! Voici comment configurer.

## 🎯 Options disponibles

### 1. **Mode Local (Par défaut)** ✅
- **Avantage**: Gratuit, aucune configuration
- **Inconvénient**: Réponses limitées et préprogrammées
- **Configuration**: Aucune, déjà actif

### 2. **Groq (Recommandé)** 🚀
- **Avantage**: Gratuit, très rapide, modèles puissants
- **Modèles**: Llama 3.3 70B, Mixtral, etc.
- **Vitesse**: Ultra-rapide (jusqu'à 800 tokens/sec)

### 3. **OpenAI (GPT)** 💰
- **Avantage**: Très intelligent, naturel
- **Inconvénient**: Payant (environ $0.002 par requête)
- **Modèles**: GPT-3.5-turbo, GPT-4

---

## 🔧 Configuration Groq (Gratuit & Recommandé)

### Étape 1: Obtenir une clé API Groq

1. Allez sur: https://console.groq.com/keys
2. Créez un compte gratuit (avec Google/GitHub)
3. Cliquez sur "Create API Key"
4. Copiez votre clé API

### Étape 2: Configurer le chatbot

Ouvrez le fichier `.env` et modifiez:

```env
# Configuration IA
AI_PROVIDER=groq

# Collez votre clé API ici
GROQ_API_KEY=gsk_votre_cle_api_ici

# Modèle à utiliser (options ci-dessous)
AI_MODEL=llama-3.3-70b-versatile
```

### Modèles Groq disponibles:

| Modèle | Description | Vitesse |
|--------|-------------|---------|
| `llama-3.3-70b-versatile` | **Recommandé** - Puissant et polyvalent | ⚡⚡⚡ |
| `llama-3.1-8b-instant` | Plus rapide, moins puissant | ⚡⚡⚡⚡ |
| `mixtral-8x7b-32768` | Bon équilibre | ⚡⚡⚡ |
| `gemma2-9b-it` | Compact et efficace | ⚡⚡⚡⚡ |

### Étape 3: Redémarrer

Le serveur se recharge automatiquement. Vous devriez voir:
```
✅ IA activée: Groq avec modèle llama-3.3-70b-versatile
```

---

## 🔧 Configuration OpenAI (Payant)

### Étape 1: Obtenir une clé API OpenAI

1. Allez sur: https://platform.openai.com/api-keys
2. Créez un compte et ajoutez des crédits
3. Créez une clé API
4. Copiez votre clé

### Étape 2: Configurer le chatbot

Modifiez `.env`:

```env
AI_PROVIDER=openai
OPENAI_API_KEY=sk-votre_cle_api_ici
AI_MODEL=gpt-3.5-turbo
```

### Modèles OpenAI:

- `gpt-3.5-turbo` - Rapide et économique
- `gpt-4` - Plus intelligent mais plus cher
- `gpt-4-turbo` - Bon équilibre

---

## 🧪 Test de l'IA

Une fois configuré, testez avec:

- "Explique-moi la relativité"
- "Écris-moi un poème sur Python"
- "Quelle est la capitale du Japon et son histoire?"
- "Aide-moi à débugger ce code"

Le chatbot utilisera l'IA pour répondre intelligemment!

---

## 🔄 Ordre de priorité des réponses

1. **Calculs mathématiques** (5 + 3)
2. **Heure/Date** (quelle heure est-il?)
3. **IA externe** (Groq/OpenAI si configuré)
4. **Base de connaissances locale** (salutations, blagues)
5. **Réponses par défaut**

---

## ⚙️ Configuration avancée

### Température (créativité)
Modifiez dans `main.py`:
```python
temperature=0.7  # 0.0 = précis, 1.0 = créatif
```

### Longueur des réponses
```python
max_tokens=500  # Nombre max de mots
```

### Historique
Le chatbot se souvient des 10 derniers messages automatiquement.

---

## 🆘 Dépannage

### "Mode local activé" alors que j'ai configuré Groq
- Vérifiez que `GROQ_API_KEY` est bien définie dans `.env`
- Vérifiez qu'il n'y a pas d'espace avant/après la clé
- Redémarrez le serveur complètement

### Erreur "Invalid API Key"
- Votre clé API est incorrecte ou expirée
- Générez une nouvelle clé

### Réponses lentes
- Normal pour OpenAI (2-3 secondes)
- Groq devrait être très rapide (<1 seconde)
- Vérifiez votre connexion internet

---

## 💡 Conseils

1. **Groq est gratuit** - Commencez par là!
2. **Limites gratuites** - Groq a des limites raisonnables
3. **Sécurité** - Ne partagez jamais vos clés API
4. **Git** - Le fichier `.env` est dans `.gitignore`

---

## 📊 Comparaison

| Feature | Local | Groq | OpenAI |
|---------|-------|------|--------|
| Prix | Gratuit | Gratuit | Payant |
| Intelligence | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Vitesse | ⚡⚡⚡⚡ | ⚡⚡⚡⚡⚡ | ⚡⚡⚡ |
| Configuration | Aucune | Facile | Facile |
| Limite | Aucune | Raisonnable | Selon paiement |

---

**Recommandation**: Commencez avec **Groq** (gratuit + puissant)! 🚀
