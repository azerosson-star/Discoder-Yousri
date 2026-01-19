"""
Schémas Pydantic pour la validation des données
"""
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import datetime


# Schémas pour les messages
class MessageBase(BaseModel):
    role: str = Field(..., description="Role: 'user' ou 'assistant'")
    content: str = Field(..., description="Contenu du message")

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    conversation_id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


# Schémas pour les conversations
class ConversationBase(BaseModel):
    conversation_id: str
    user_name: Optional[str] = None

class ConversationCreate(BaseModel):
    user_name: Optional[str] = None

class ConversationResponse(ConversationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# Schémas pour les requêtes de chat
class ChatRequest(BaseModel):
    message: str = Field(..., description="Message de l'utilisateur")
    conversation_id: Optional[str] = None
    user_name: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    timestamp: str
    message_id: Optional[int] = None


# Schémas pour le contexte utilisateur
class UserContextBase(BaseModel):
    conversation_id: str
    user_name: Optional[str] = None
    preferences: Optional[str] = None

class UserContextCreate(UserContextBase):
    pass

class UserContextResponse(UserContextBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Schéma pour lister les conversations
class ConversationListResponse(BaseModel):
    id: int
    conversation_id: str
    user_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    message_count: int = 0

    model_config = ConfigDict(from_attributes=True)
