"""
Configuration de la base de données SQLite avec SQLAlchemy
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

# URL de la base de données SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./chatbot.db")

# Logs SQL (très verbeux) : activable via SQL_ECHO=true
SQL_ECHO = os.getenv("SQL_ECHO", "false").strip().lower() in {"1", "true", "yes", "y", "on"}

# Créer le moteur async
engine = create_async_engine(
    DATABASE_URL,
    echo=SQL_ECHO,
    future=True
)

# Session maker
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base pour les modèles
Base = declarative_base()

# Dépendance pour obtenir une session de base de données
async def get_db():
    """
    Dépendance FastAPI pour obtenir une session de base de données
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Fonction pour créer les tables
async def create_tables():
    """
    Créer toutes les tables dans la base de données
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Fonction pour supprimer les tables (utile pour le développement)
async def drop_tables():
    """
    Supprimer toutes les tables de la base de données
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
