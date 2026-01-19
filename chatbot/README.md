# Chatbot FastAPI

Un chatbot intelligent construit avec FastAPI et Python.

## 🚀 Fonctionnalités

- API REST complète avec FastAPI
- Interface web interactive
- Gestion des conversations multiples
- Historique des messages
- Base de connaissances extensible
- Réponses contextuelles

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## 🔧 Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

1. Lancer le serveur :
```bash
python main.py
```

Ou avec uvicorn directement :
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Ouvrir votre navigateur à l'adresse :
```
http://localhost:8000
```

3. Accéder à la documentation API interactive :
```
http://localhost:8000/docs
```

## 🔌 Endpoints API

### POST /api/chat
Envoyer un message au chatbot
```json
{
  "message": "Bonjour!",
  "conversation_id": "optional"
}
```

### GET /api/conversation/{conversation_id}
Récupérer l'historique d'une conversation

### DELETE /api/conversation/{conversation_id}
Supprimer une conversation

### GET /api/conversations
Lister toutes les conversations

### GET /health
Vérifier l'état du serveur

## 🛠️ Développement

Pour étendre la base de connaissances, modifiez le dictionnaire `knowledge_base` dans `main.py`.

Pour personnaliser l'interface, modifiez les fichiers dans le dossier `static/`.

## 📝 License

MIT
