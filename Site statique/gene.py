import os

# ==========================================
# CONTENU DES FICHIERS CSS (Communs)
# ==========================================

css_global = """/* Reset et Variables */
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --primary: #0056b3; --bg: #f4f4f4; --text: #333; --white: #fff; --dark: #222; }
body { font-family: sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }

/* Classes Utilitaires */
.container { max-width: 1200px; margin: 0 auto; padding: 1rem; }
.flex { display: flex; } .flex-col { flex-direction: column; } .flex-grow { flex-grow: 1; }
.wrap { flex-wrap: wrap; } .gap-1 { gap: 1rem; } .gap-2 { gap: 2rem; }
.align-center { align-items: center; } .justify-between { justify-content: space-between; }
.p-1 { padding: 1rem; } .p-2 { padding: 2rem; } .m-1 { margin: 1rem; } .mb-1 { margin-bottom: 1rem; }
.bg-white { background: var(--white); } .bg-dark { background: var(--dark); color: var(--white); } 
.bg-primary { background: var(--primary); color: var(--white); }
.text-center { text-align: center; } .td-none { text-decoration: none; color: inherit; }
.br-1 { border-radius: 8px; } .shadow { box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
.fixed { position: fixed; } .bottom-0 { bottom: 20px; } .right-0 { right: 20px; }
.h-100vh { height: 100vh; } .w-sidebar { width: 250px; } .ml-sidebar { margin-left: 250px; }

/* Checkbox Hack - Base 100% CSS */
.toggle-checkbox { display: none; }

/* Widget IA (Frame) */
.ai-btn { cursor: pointer; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; z-index: 100; transition: transform 0.2s;}
.ai-btn:hover { transform: scale(1.1); }
.ai-frame { display: none; width: 320px; height: 400px; bottom: 90px; right: 20px; z-index: 99; overflow-y: auto; }
.toggle-checkbox:checked ~ .ai-frame { display: flex; }
.chat-bubble { padding: 10px; border-radius: 10px; margin-bottom: 10px; max-width: 80%; }
.chat-left { background: #e9ecef; align-self: flex-start; color: black; }
.chat-right { background: var(--primary); color: white; align-self: flex-end; }
"""

css_forms = """/* Styles spécifiques aux formulaires */
.form-group { display: flex; flex-direction: column; margin-bottom: 1rem; }
.form-label { font-weight: bold; margin-bottom: 0.5rem; }
.form-input { padding: 0.7rem; border: 1px solid #ccc; border-radius: 4px; font-family: inherit; }
.form-row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.btn { padding: 0.8rem 1.5rem; border: none; cursor: pointer; font-weight: bold; }
.btn:hover { opacity: 0.9; }
"""

css_products = """/* Styles pour les produits (Liste et Cartes) */
/* Liste (Site 1) */
.prod-list { display: flex; flex-direction: column; gap: 10px; }
.prod-row { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #ddd; padding: 10px; }
.prod-badge { background: #eee; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem; }

/* Grille/Cartes (Site 2) */
.prod-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
.prod-card { border: 1px solid #ddd; display: flex; flex-direction: column; justify-content: space-between; }
.prod-img-ph { height: 150px; background: #ccc; border-radius: 8px 8px 0 0; }
"""

css_responsive = """/* Media Queries Minimalistes (Surcharges uniquement) */
@media (max-width: 768px) {
    /* Site 1 : Navbar horizontale vers icônes */
    .nav-text { display: none; }
    .nav-icon::after { content: attr(data-icon); font-size: 1.5rem; }
    
    /* Site 2 : Sidebar vers Menu Burger (Checkbox Hack) */
    .sidebar { transform: translateX(-100%); transition: transform 0.3s ease; position: fixed; top: 0; left: 0; z-index: 50; }
    .menu-toggle:checked ~ .sidebar { transform: translateX(0); }
    .burger-btn { display: block !important; cursor: pointer; font-size: 2rem; padding: 10px; position: fixed; top: 10px; left: 10px; z-index: 60; background: var(--dark); color: white; border-radius: 5px;}
    .ml-sidebar { margin-left: 0 !important; }
    .pt-mobile { padding-top: 70px !important; }

    /* Produits Liste Mobile */
    .prod-row { flex-direction: column; align-items: flex-start; gap: 5px; }
}

@media (min-width: 769px) {
    .burger-btn, .menu-toggle { display: none; }
}
"""

# ==========================================
# CONTENU HTML - SITE 1 (Nav Horizontale, Liste)
# ==========================================
html_s1_header = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site 1</title>
    <link rel="stylesheet" href="../css/global.css">
    <link rel="stylesheet" href="../css/forms.css">
    <link rel="stylesheet" href="../css/products.css">
    <link rel="stylesheet" href="../css/responsive.css">
</head>
<body>
    <header class="bg-dark p-1">
        <nav class="flex justify-between align-center container">
            <h2>Site 1</h2>
            <div class="flex gap-1">
                <a href="index.html" class="td-none nav-icon" data-icon="🏠"><span class="nav-text">Accueil</span></a>
                <a href="produits.html" class="td-none nav-icon" data-icon="📦"><span class="nav-text">Produits</span></a>
                <a href="contact.html" class="td-none nav-icon" data-icon="✉️"><span class="nav-text">Contact</span></a>
            </div>
        </nav>
    </header>
    <main class="container">
"""

html_s1_index = html_s1_header + """
        <h1 class="mb-1 text-center">Bienvenue sur le Site 1</h1>
        <p class="text-center p-2 bg-white br-1 shadow">Ceci est une page d'accueil avec du texte fixe. Notre navbar devient des icônes sur mobile.</p>
        
        <input type="checkbox" id="ai-toggle" class="toggle-checkbox">
        <label for="ai-toggle" class="ai-btn bg-primary fixed bottom-0 right-0 shadow">💬</label>
        
        <div class="ai-frame fixed bg-white shadow br-1 p-1 flex-col">
            <h3 class="mb-1">Assistant IA</h3>
            <div class="chat-bubble chat-left">Bonjour ! Je suis une IA générée en pur CSS.</div>
            <div class="chat-bubble chat-right">Impressionnant ! Comment ça marche ?</div>
            <div class="chat-bubble chat-left">Grâce au Checkbox Hack !</div>
        </div>
    </main>
</body>
</html>"""

html_s1_produits = html_s1_header + """
        <h1 class="mb-1">Nos Articles (Vue Liste)</h1>
        <div class="prod-list bg-white br-1 shadow p-1">
            <div class="prod-row">
                <strong>Clavier Mécanique</strong>
                <span class="prod-badge">Réf: CLV-01</span>
                <span class="prod-badge">EAN: 123456789</span>
                <span class="prod-badge">Stock: 42</span>
                <strong>45,00 €</strong>
            </div>
            <div class="prod-row">
                <strong>Souris Sans Fil</strong>
                <span class="prod-badge">Réf: SRS-02</span>
                <span class="prod-badge">EAN: 987654321</span>
                <span class="prod-badge">Stock: 15</span>
                <strong>25,50 €</strong>
            </div>
        </div>
    </main>
</body>
</html>"""

html_s1_contact = html_s1_header + """
        <h1 class="mb-1">Contactez-nous</h1>
        <form class="bg-white p-2 br-1 shadow flex flex-col">
            <div class="form-group">
                <label class="form-label">Nom complet</label>
                <input type="text" class="form-input" placeholder="Votre nom">
            </div>
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="nom@domaine.com">
            </div>
            <div class="form-group">
                <label class="form-label">Mot de passe</label>
                <input type="password" class="form-input">
            </div>
            <div class="form-group">
                <label class="form-label">Sujet</label>
                <select class="form-input">
                    <option>Question technique</option>
                    <option>Service client</option>
                </select>
            </div>
            <div class="form-row mb-1">
                <label class="form-label mr-1">Priorité :</label>
                <input type="radio" name="prio" id="p1" checked> <label for="p1">Basse</label>
                <input type="radio" name="prio" id="p2"> <label for="p2">Haute</label>
            </div>
            <div class="form-row mb-1">
                <input type="checkbox" id="rgpd"> <label for="rgpd">J'accepte la politique de confidentialité</label>
            </div>
            <button type="submit" class="btn bg-primary br-1">Envoyer le message</button>
        </form>
    </main>
</body>
</html>"""


# ==========================================
# CONTENU HTML - SITE 2 (Nav Verticale, Cartes)
# ==========================================
html_s2_header_top = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site 2</title>
    <link rel="stylesheet" href="../css/global.css">
    <link rel="stylesheet" href="../css/forms.css">
    <link rel="stylesheet" href="../css/products.css">
    <link rel="stylesheet" href="../css/responsive.css">
</head>
<body class="flex">
    <input type="checkbox" id="nav-toggle" class="menu-toggle">
    <label for="nav-toggle" class="burger-btn bg-dark" style="display:none;">☰</label>

    <nav class="sidebar bg-dark p-2 flex flex-col h-100vh w-sidebar gap-1 fixed">
        <h2>Site 2</h2>
        <a href="index.html" class="td-none">Accueil</a>
        <a href="produits.html" class="td-none">Produits</a>
        <a href="contact.html" class="td-none">Contact</a>
    </nav>
    <main class="flex-grow p-2 ml-sidebar pt-mobile">
"""

html_s2_index = html_s2_header_top + """
        <h1 class="mb-1">Accueil du Site 2</h1>
        <p class="p-2 bg-white br-1 shadow">Ici la navigation est latérale. Sur petit écran, elle disparait pour laisser place à un bouton burger 100% fonctionnel sans JS.</p>
        
        <input type="checkbox" id="ai-toggle" class="toggle-checkbox">
        <label for="ai-toggle" class="ai-btn bg-primary fixed bottom-0 right-0 shadow">💬</label>
        <div class="ai-frame fixed bg-white shadow br-1 p-1 flex-col">
            <h3 class="mb-1">Assistant IA</h3>
            <div class="chat-bubble chat-left">Bonjour de l'IA du site 2 !</div>
        </div>
    </main>
</body>
</html>"""

html_s2_produits = html_s2_header_top + """
        <h1 class="mb-1">Nos Articles (Vue Cartes)</h1>
        <div class="prod-grid">
            <div class="prod-card bg-white br-1 shadow">
                <div class="prod-img-ph"></div>
                <div class="p-1 flex flex-col gap-1">
                    <h3>Écran 27"</h3>
                    <div class="flex justify-between"><span>Réf: ECR-01</span> <span>EAN: 112233</span></div>
                    <div class="flex justify-between"><span>Stock: 8</span> <strong>199,99 €</strong></div>
                </div>
            </div>
            <div class="prod-card bg-white br-1 shadow">
                <div class="prod-img-ph"></div>
                <div class="p-1 flex flex-col gap-1">
                    <h3>Casque Audio</h3>
                    <div class="flex justify-between"><span>Réf: CSQ-02</span> <span>EAN: 445566</span></div>
                    <div class="flex justify-between"><span>Stock: 21</span> <strong>89,00 €</strong></div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>"""

html_s2_contact = html_s2_header_top + """
        <h1 class="mb-1">Contact</h1>
        <form class="bg-white p-2 br-1 shadow flex flex-col">
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="nom@domaine.com">
            </div>
            <div class="form-group">
                <label class="form-label">Message</label>
                <input type="text" class="form-input" style="height: 100px;">
            </div>
            <button type="submit" class="btn bg-primary br-1">Envoyer</button>
        </form>
    </main>
</body>
</html>"""

# ==========================================
# CREATION DES DOSSIERS ET FICHIERS
# ==========================================

def creer_fichier(chemin, contenu):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)
    print(f"✔️ Fichier créé : {chemin}")

def main():
    base_dir = "mon_projet_web"
    dirs = [
        f"{base_dir}/css",
        f"{base_dir}/site1",
        f"{base_dir}/site2"
    ]
    
    # Création des dossiers
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    # Écriture CSS
    creer_fichier(f"{base_dir}/css/global.css", css_global)
    creer_fichier(f"{base_dir}/css/forms.css", css_forms)
    creer_fichier(f"{base_dir}/css/products.css", css_products)
    creer_fichier(f"{base_dir}/css/responsive.css", css_responsive)
    
    # Écriture Site 1
    creer_fichier(f"{base_dir}/site1/index.html", html_s1_index)
    creer_fichier(f"{base_dir}/site1/produits.html", html_s1_produits)
    creer_fichier(f"{base_dir}/site1/contact.html", html_s1_contact)
    
    # Écriture Site 2
    creer_fichier(f"{base_dir}/site2/index.html", html_s2_index)
    creer_fichier(f"{base_dir}/site2/produits.html", html_s2_produits)
    creer_fichier(f"{base_dir}/site2/contact.html", html_s2_contact)
    
    print("\n🚀 Succès ! Ton projet a été généré et rangé dans le dossier 'mon_projet_web'.")

if __name__ == "__main__":
    main()