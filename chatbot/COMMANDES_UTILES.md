# 🔧 Commandes Utiles - Chatbot FastAPI

## 🚀 Démarrage

```powershell
# Méthode 1: Script automatique
.\start.bat

# Méthode 2: Direct
python main.py

# Méthode 3: Avec Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📦 Installation

```powershell
# Installer toutes les dépendances
pip install -r requirements.txt

# Installer individuellement
pip install fastapi uvicorn sqlalchemy aiosqlite pydantic python-dotenv

# Vérifier l'installation
python -c "import fastapi, sqlalchemy; print('OK')"
```

## 🧪 Tests

```powershell
# Tests base de données
python test_database.py

# Exemples d'utilisation
python examples_usage.py

# Test avec script
.\test.bat

# Test API avec curl
curl -X POST http://localhost:8000/api/chat -H "Content-Type: application/json" -d '{\"message\":\"test\"}'
```

## 🗄️ Base de Données

```powershell
# Voir la structure
sqlite3 chatbot.db ".schema"

# Compter les conversations
sqlite3 chatbot.db "SELECT COUNT(*) FROM conversations;"

# Voir les derniers messages
sqlite3 chatbot.db "SELECT * FROM messages ORDER BY timestamp DESC LIMIT 10;"

# Backup
Copy-Item chatbot.db "backup/chatbot_$(Get-Date -Format 'yyyyMMdd_HHmmss').db"

# Supprimer la base (attention!)
Remove-Item chatbot.db

# Réinitialiser
python -c "from database import drop_tables, create_tables; import asyncio; asyncio.run(drop_tables()); asyncio.run(create_tables())"
```

## 📊 Statistiques

```powershell
# Via API
curl http://localhost:8000/api/stats

# Via Python
python -c "import requests; print(requests.get('http://localhost:8000/api/stats').json())"
```

## 🔍 Debugging

```powershell
# Voir les logs du serveur
python main.py

# Vérifier le port
netstat -ano | findstr :8000

# Tuer le processus sur le port 8000
$process = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
if ($process) { Stop-Process -Id $process -Force }

# Vérifier Python
python --version

# Vérifier les modules
pip list | findstr -i "fastapi sqlalchemy"
```

## 🧹 Nettoyage

```powershell
# Supprimer cache Python
Remove-Item -Recurse -Force __pycache__
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force

# Supprimer base de données
Remove-Item chatbot.db -ErrorAction SilentlyContinue

# Réinstaller dépendances
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

## 🌐 Tests API

### Chat
```powershell
# Envoyer un message
curl -X POST http://localhost:8000/api/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "Bonjour!", "user_name": "Test"}'

# Avec PowerShell
Invoke-RestMethod -Uri http://localhost:8000/api/chat -Method Post -ContentType "application/json" -Body '{"message":"Bonjour!"}'
```

### Conversations
```powershell
# Lister
curl http://localhost:8000/api/conversations

# Récupérer une conversation
curl http://localhost:8000/api/conversation/CONVERSATION_ID

# Supprimer
curl -X DELETE http://localhost:8000/api/conversation/CONVERSATION_ID
```

### Health Check
```powershell
curl http://localhost:8000/health
```

## 📈 Performance

```powershell
# Tester la charge (nécessite Apache Bench)
ab -n 1000 -c 10 http://localhost:8000/health

# Avec PowerShell (simple)
Measure-Command { 
    1..100 | ForEach-Object { 
        Invoke-WebRequest http://localhost:8000/health 
    } 
}
```

## 🔧 Configuration

```powershell
# Créer fichier .env
Copy-Item .env.example .env

# Éditer la configuration
notepad .env

# Vérifier les variables
Get-Content .env
```

## 📦 Migration PostgreSQL

```powershell
# Installer le driver
pip install asyncpg psycopg2-binary

# Modifier .env
Set-Content .env "DATABASE_URL=postgresql+asyncpg://user:pass@localhost/chatbot"

# Créer la base PostgreSQL
psql -U postgres -c "CREATE DATABASE chatbot;"
```

## 🚀 Déploiement

```powershell
# Production avec Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Avec Gunicorn (Linux)
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📝 Logs

```powershell
# Rediriger vers fichier
python main.py > logs/chatbot.log 2>&1

# Voir logs en temps réel
Get-Content logs/chatbot.log -Wait

# Filtrer erreurs
Get-Content logs/chatbot.log | Select-String "ERROR"
```

## 🎯 Raccourcis

```powershell
# Tout en un: clean + install + test + run
Remove-Item -Recurse -Force __pycache__; `
pip install -r requirements.txt; `
python test_database.py; `
python main.py

# Quick restart
taskkill /F /IM python.exe; python main.py
```

## 📊 Monitoring

```powershell
# Voir l'utilisation CPU/Mémoire
Get-Process python | Select-Object CPU, WorkingSet, ProcessName

# Surveiller les connexions
netstat -ano | findstr :8000

# Logs système
Get-EventLog -LogName Application -Source Python -Newest 10
```

## 🔐 Sécurité

```powershell
# Vérifier les dépendances vulnérables
pip install safety
safety check

# Mettre à jour les packages
pip list --outdated
pip install --upgrade package_name
```

## 💡 Astuces

```powershell
# Ouvrir rapidement dans le navigateur
Start-Process http://localhost:8000

# Documentation API
Start-Process http://localhost:8000/docs

# Voir la structure du projet
tree /F /A

# Compter les lignes de code
(Get-Content *.py | Measure-Object -Line).Lines
```
