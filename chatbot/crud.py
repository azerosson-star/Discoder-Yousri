"""
Opérations CRUD (Create, Read, Update, Delete) pour la base de données
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Optional, List
import uuid
from datetime import datetime

from models import Conversation, Message, UserContext
from schemas import MessageCreate, ConversationCreate, UserContextCreate


# =====================================================
# CRUD pour les Conversations
# =====================================================

async def create_conversation(
    db: AsyncSession,
    user_name: Optional[str] = None
) -> Conversation:
    """
    Créer une nouvelle conversation
    """
    conversation_id = str(uuid.uuid4())
    conversation = Conversation(
        conversation_id=conversation_id,
        user_name=user_name
    )
    db.add(conversation)
    await db.commit()
    await db.refresh(conversation)
    return conversation


async def get_conversation(
    db: AsyncSession,
    conversation_id: str
) -> Optional[Conversation]:
    """
    Récupérer une conversation par son ID
    """
    result = await db.execute(
        select(Conversation)
        .options(selectinload(Conversation.messages))
        .where(Conversation.conversation_id == conversation_id)
    )
    return result.scalar_one_or_none()


async def get_conversations(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100
) -> List[Conversation]:
    """
    Récupérer toutes les conversations avec pagination
    """
    result = await db.execute(
        select(Conversation)
        .options(selectinload(Conversation.messages))
        .order_by(Conversation.updated_at.desc())
        .offset(skip)
        .limit(limit)
    )
    return list(result.scalars().all())


async def delete_conversation(
    db: AsyncSession,
    conversation_id: str
) -> bool:
    """
    Supprimer une conversation
    """
    conversation = await get_conversation(db, conversation_id)
    if conversation:
        await db.delete(conversation)
        await db.commit()
        return True
    return False


# =====================================================
# CRUD pour les Messages
# =====================================================

async def create_message(
    db: AsyncSession,
    conversation_id: str,
    role: str,
    content: str
) -> Message:
    """
    Créer un nouveau message dans une conversation
    """
    # Récupérer la conversation
    conversation = await get_conversation(db, conversation_id)
    
    if not conversation:
        # Si la conversation n'existe pas, la créer
        conversation = await create_conversation(db)
    
    # Créer le message
    message = Message(
        conversation_id=conversation.id,
        role=role,
        content=content,
        timestamp=datetime.utcnow()
    )
    db.add(message)
    
    # Mettre à jour le timestamp de la conversation
    conversation.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(message)
    return message


async def get_messages(
    db: AsyncSession,
    conversation_id: str
) -> List[Message]:
    """
    Récupérer tous les messages d'une conversation
    """
    conversation = await get_conversation(db, conversation_id)
    if not conversation:
        return []
    
    result = await db.execute(
        select(Message)
        .where(Message.conversation_id == conversation.id)
        .order_by(Message.timestamp.asc())
    )
    return list(result.scalars().all())


async def get_message_count(
    db: AsyncSession,
    conversation_db_id: int
) -> int:
    """
    Compter le nombre de messages dans une conversation
    """
    result = await db.execute(
        select(func.count(Message.id))
        .where(Message.conversation_id == conversation_db_id)
    )
    return result.scalar_one()


# =====================================================
# CRUD pour le Contexte Utilisateur
# =====================================================

async def create_or_update_user_context(
    db: AsyncSession,
    conversation_id: str,
    user_name: Optional[str] = None,
    preferences: Optional[str] = None
) -> UserContext:
    """
    Créer ou mettre à jour le contexte utilisateur
    """
    # Vérifier si le contexte existe déjà
    result = await db.execute(
        select(UserContext)
        .where(UserContext.conversation_id == conversation_id)
    )
    context = result.scalar_one_or_none()
    
    if context:
        # Mettre à jour
        if user_name is not None:
            context.user_name = user_name
        if preferences is not None:
            context.preferences = preferences
        context.updated_at = datetime.utcnow()
    else:
        # Créer
        context = UserContext(
            conversation_id=conversation_id,
            user_name=user_name,
            preferences=preferences
        )
        db.add(context)
    
    await db.commit()
    await db.refresh(context)
    return context


async def get_user_context(
    db: AsyncSession,
    conversation_id: str
) -> Optional[UserContext]:
    """
    Récupérer le contexte utilisateur
    """
    result = await db.execute(
        select(UserContext)
        .where(UserContext.conversation_id == conversation_id)
    )
    return result.scalar_one_or_none()


# =====================================================
# Utilitaires
# =====================================================

async def get_conversation_stats(db: AsyncSession) -> dict:
    """
    Obtenir des statistiques sur les conversations
    """
    # Nombre total de conversations
    result = await db.execute(select(func.count(Conversation.id)))
    total_conversations = result.scalar_one()
    
    # Nombre total de messages
    result = await db.execute(select(func.count(Message.id)))
    total_messages = result.scalar_one()
    
    return {
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "average_messages_per_conversation": (
            total_messages / total_conversations if total_conversations > 0 else 0
        )
    }
