# 🗄️ Base de Données SQL - Documentation

## Vue d'ensemble

Ce chatbot utilise **SQLite** avec **SQLAlchemy** (mode asynchrone) pour persister les conversations et les messages.

## 📊 Structure de la Base de Données

### Table: `conversations`
Stocke les métadonnées des conversations.

| Colonne | Type | Description |
|---------|------|-------------|
| id | Integer | Clé primaire auto-incrémentée |
| conversation_id | String(100) | ID unique de la conversation (UUID) |
| created_at | DateTime | Date de création |
| updated_at | DateTime | Date de dernière mise à jour |
| user_name | String(100) | Nom de l'utilisateur (optionnel) |

**Index:** `conversation_id` (unique)

### Table: `messages`
Stocke tous les messages d'une conversation.

| Colonne | Type | Description |
|---------|------|-------------|
| id | Integer | Clé primaire auto-incrémentée |
| conversation_id | Integer | Clé étrangère vers `conversations.id` |
| role | String(20) | "user" ou "assistant" |
| content | Text | Contenu du message |
| timestamp | DateTime | Date et heure du message |

**Relations:** 
- `conversation_id` → `conversations.id` (CASCADE DELETE)

### Table: `user_contexts`
Stocke les préférences et le contexte utilisateur.

| Colonne | Type | Description |
|---------|------|-------------|
| id | Integer | Clé primaire auto-incrémentée |
| conversation_id | String(100) | ID unique de la conversation |
| user_name | String(100) | Nom de l'utilisateur |
| preferences | Text | Préférences JSON |
| created_at | DateTime | Date de création |
| updated_at | DateTime | Date de mise à jour |

## 🔧 Configuration

### Variable d'Environnement

Ajoutez dans votre fichier `.env`:

```env
# Base de données (SQLite par défaut)
DATABASE_URL=sqlite+aiosqlite:///./chatbot.db
```

Pour **PostgreSQL** (production):
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/chatbot_db
```

Pour **MySQL**:
```env
DATABASE_URL=mysql+aiomysql://user:password@localhost/chatbot_db
```

## 📁 Fichiers Créés

```
chatbot/
├── database.py          # Configuration de la connexion DB
├── models.py            # Modèles SQLAlchemy (tables)
├── schemas.py           # Schémas Pydantic (validation)
├── crud.py              # Opérations CRUD
├── main.py              # Application FastAPI (mise à jour)
├── chatbot.db           # Base de données SQLite (créée automatiquement)
└── DATABASE_README.md   # Ce fichier
```

## 🚀 Installation

1. **Installer les dépendances:**

```powershell
pip install -r requirements.txt
```

2. **Lancer l'application:**

```powershell
python main.py
```

La base de données sera créée automatiquement au premier démarrage.

## 📡 API Endpoints

### Chat

**POST** `/api/chat`
```json
{
  "message": "Bonjour!",
  "conversation_id": "optional-uuid",
  "user_name": "Jean"
}
```

**Réponse:**
```json
{
  "response": "Bonjour! Ravi de vous parler...",
  "conversation_id": "abc-123-def",
  "timestamp": "2026-01-19T10:30:00",
  "message_id": 42
}
```

### Conversations

**GET** `/api/conversations?skip=0&limit=100`
Liste toutes les conversations avec pagination.

**GET** `/api/conversation/{conversation_id}`
Récupère une conversation spécifique avec tous ses messages.

**DELETE** `/api/conversation/{conversation_id}`
Supprime une conversation et tous ses messages.

### Statistiques

**GET** `/api/stats`
```json
{
  "status": "success",
  "statistics": {
    "total_conversations": 150,
    "total_messages": 842,
    "average_messages_per_conversation": 5.61
  },
  "timestamp": "2026-01-19T10:30:00"
}
```

## 🔍 Opérations CRUD Disponibles

### Dans `crud.py`:

#### Conversations
- `create_conversation(db, user_name)` - Créer une conversation
- `get_conversation(db, conversation_id)` - Récupérer une conversation
- `get_conversations(db, skip, limit)` - Liste avec pagination
- `delete_conversation(db, conversation_id)` - Supprimer

#### Messages
- `create_message(db, conversation_id, role, content)` - Créer un message
- `get_messages(db, conversation_id)` - Récupérer tous les messages
- `get_message_count(db, conversation_db_id)` - Compter les messages

#### Contexte Utilisateur
- `create_or_update_user_context(db, conversation_id, user_name, preferences)`
- `get_user_context(db, conversation_id)`

#### Statistiques
- `get_conversation_stats(db)` - Statistiques globales

## 💾 Exemple d'Utilisation Direct

```python
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
import crud

async def example():
    async with AsyncSessionLocal() as db:
        # Créer une conversation
        conv = await crud.create_conversation(db, user_name="Alice")
        
        # Ajouter un message
        msg = await crud.create_message(
            db,
            conversation_id=conv.conversation_id,
            role="user",
            content="Bonjour!"
        )
        
        # Récupérer les messages
        messages = await crud.get_messages(db, conv.conversation_id)
        for msg in messages:
            print(f"{msg.role}: {msg.content}")
```

## 🔒 Sécurité

### Bonnes Pratiques

1. **Production**: Utilisez PostgreSQL ou MySQL au lieu de SQLite
2. **Sauvegarde**: Configurez des backups réguliers de `chatbot.db`
3. **Validation**: Les schémas Pydantic valident automatiquement les données
4. **Transactions**: SQLAlchemy gère les transactions automatiquement

### Backup de la Base de Données

**SQLite:**
```powershell
# Copie simple
Copy-Item chatbot.db chatbot_backup.db

# Avec timestamp
$date = Get-Date -Format "yyyyMMdd_HHmmss"
Copy-Item chatbot.db "chatbot_backup_$date.db"
```

## 🛠️ Maintenance

### Réinitialiser la Base de Données

```python
from database import drop_tables, create_tables
import asyncio

async def reset_db():
    await drop_tables()
    await create_tables()

asyncio.run(reset_db())
```

Ou simplement supprimer le fichier:
```powershell
Remove-Item chatbot.db
```

### Migrations (Alembic)

Pour des migrations plus avancées:

```powershell
pip install alembic
alembic init alembic
```

## 📈 Performance

- **SQLite**: Parfait pour le développement et petites applications
- **PostgreSQL**: Recommandé pour la production
- **Indexation**: Les colonnes importantes sont indexées
- **Async**: Support asynchrone complet avec `aiosqlite`

## 🐛 Dépannage

### Erreur "no such table"
La base de données n'a pas été initialisée. Redémarrez l'application.

### Erreur "database is locked"
SQLite limite les écritures concurrentes. Utilisez PostgreSQL en production.

### Voir les requêtes SQL
Dans `database.py`, `echo=True` affiche toutes les requêtes SQL.

## 📚 Documentation Complète

- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **FastAPI + Databases**: https://fastapi.tiangolo.com/tutorial/sql-databases/
- **Pydantic**: https://docs.pydantic.dev/

---

✅ **Base de données configurée et prête à l'emploi!**
