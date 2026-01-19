# 🤖 Chatbot Intelligent - FastAPI + SQL

Chatbot moderne avec interface web, base de données SQL et support IA externe.

## ✨ Fonctionnalités Principales

- 💬 **Interface web moderne** - Design responsive et intuitif
- 🗄️ **Base de données SQL** - Persistance complète des conversations (SQLite/PostgreSQL)
- 🤖 **Support IA** - Groq (gratuit) ou OpenAI
- 📊 **Statistiques** - Analytics sur vos conversations
- 🔄 **API REST** - Endpoints complets pour intégration
- ⚡ **Asynchrone** - Performances optimales
- 🎯 **Mode local** - Fonctionne sans IA externe

## 🚀 Démarrage en 30 Secondes

### Windows (Double-clic)
```
start.bat
```

### Ligne de Commande
```powershell
pip install -r requirements.txt
python main.py
```

Ouvrez: **http://localhost:8000**

## 📦 Installation Complète

```powershell
# 1. Cloner le projet
git clone <url>
cd chatbot

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Tester la base de données
python test_database.py

# 4. Lancer le serveur
python main.py
```

## 🔧 Configuration IA (Optionnel)

Copiez `.env.example` vers `.env`:

```env
AI_PROVIDER=groq
GROQ_API_KEY=votre_cle_ici
AI_MODEL=llama-3.3-70b-versatile
```

**Obtenir une clé gratuite:** https://console.groq.com/keys

## 🗄️ Base de Données

### Tables SQL
- **conversations** - Métadonnées et utilisateurs
- **messages** - Tous les messages sauvegardés
- **user_contexts** - Préférences utilisateur

### Avantages
✅ Toutes les conversations sont sauvegardées  
✅ Survit aux redémarrages  
✅ Historique complet  
✅ Recherche et statistiques  

## 📡 API Endpoints

```http
POST   /api/chat                  # Envoyer un message
GET    /api/conversations         # Liste des conversations  
GET    /api/conversation/{id}     # Récupérer une conversation
DELETE /api/conversation/{id}     # Supprimer
GET    /api/stats                 # Statistiques
GET    /health                    # Santé du serveur
```

## 📁 Structure

```
chatbot/
├── main.py              # Application FastAPI
├── database.py          # Configuration DB
├── models.py            # Modèles SQL
├── schemas.py           # Validation Pydantic
├── crud.py              # Opérations CRUD
├── static/index.html    # Interface web
├── start.bat            # Démarrage rapide
├── test.bat             # Tests
└── chatbot.db           # SQLite (auto-créée)
```

## 🛠️ Scripts Utiles

```powershell
# Démarrer le serveur
start.bat

# Tester la base de données
test.bat

# Tests manuels
python test_database.py
python examples_usage.py
```

## 📊 Exemples d'Utilisation

### API
```powershell
curl -X POST http://localhost:8000/api/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "Bonjour!"}'
```

### Python
```python
import requests

response = requests.post("http://localhost:8000/api/chat", 
    json={"message": "Bonjour!", "user_name": "Jean"})
print(response.json())
```

## 🚀 Production

### PostgreSQL
```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/chatbot
```

```powershell
pip install asyncpg
```

### Déploiement
```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📚 Documentation

- **API Interactive**: http://localhost:8000/docs
- **DATABASE_README.md** - Guide complet BDD
- **CONFIGURATION_IA.md** - Configuration IA
- **SQL_INTEGRATION_SUCCESS.md** - Guide d'intégration

## 🔒 Sécurité

- Clés API dans `.env` (git-ignoré)
- Validation Pydantic automatique
- Transactions SQL sécurisées
- CORS configurable

## 🐛 Dépannage

### Module not found
```powershell
pip install -r requirements.txt
```

### Port 8000 occupé
```powershell
netstat -ano | findstr :8000
```

### Database locked
Utilisez PostgreSQL pour la production

## 📦 Dépendances

- FastAPI - Framework web
- SQLAlchemy - ORM SQL
- Aiosqlite - SQLite async
- Uvicorn - Serveur ASGI
- Pydantic - Validation
- Groq/OpenAI - IA (optionnel)

## 💾 Backup

```powershell
# Sauvegarder SQLite
Copy-Item chatbot.db backup/chatbot_$(Get-Date -Format 'yyyyMMdd_HHmmss').db
```

## ✅ Checklist de Production

- [ ] Migrer vers PostgreSQL
- [ ] Configurer variables d'environnement
- [ ] Activer HTTPS
- [ ] Mettre en place backups automatiques
- [ ] Configurer monitoring
- [ ] Optimiser CORS

## 🤝 Contribution

Projet éducatif - Libre d'utilisation et modification

## 📝 Licence

MIT License - Utilisez librement

---

**Développé avec ❤️ - FastAPI + SQLAlchemy + Python 3.14**

🌟 **N'oubliez pas de star le projet!**
