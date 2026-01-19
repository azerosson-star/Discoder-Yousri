from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional, Dict
import uvicorn
from datetime import datetime
import json
import re
import random
import os
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI

# Charger les variables d'environnement
load_dotenv()

app = FastAPI(title="Chatbot API", version="1.0.0")

# Configuration de l'IA
AI_PROVIDER = os.getenv("AI_PROVIDER", "local").lower()
AI_MODEL = os.getenv("AI_MODEL", "llama-3.3-70b-versatile")

# Initialiser le client IA selon le provider
ai_client = None
if AI_PROVIDER == "groq":
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        ai_client = Groq(api_key=api_key)
        print(f"✅ IA activée: Groq avec modèle {AI_MODEL}")
    else:
        print("⚠️ GROQ_API_KEY non configurée, mode local activé")
        AI_PROVIDER = "local"
elif AI_PROVIDER == "openai":
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        ai_client = OpenAI(api_key=api_key)
        AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")
        print(f"✅ IA activée: OpenAI avec modèle {AI_MODEL}")
    else:
        print("⚠️ OPENAI_API_KEY non configurée, mode local activé")
        AI_PROVIDER = "local"
else:
    print("ℹ️ Mode local activé (sans IA externe)")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles de données
class Message(BaseModel):
    role: str  # "user" ou "assistant"
    content: str
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    timestamp: str

# Stockage en mémoire des conversations
conversations = {}

# Contexte utilisateur pour personnalisation
user_context = {}

# Base de connaissances avancée avec patterns et réponses multiples
knowledge_base = {
    "greetings": {
        "patterns": ["bonjour", "salut", "hello", "hey", "coucou", "bonsoir", "hi"],
        "responses": [
            "Bonjour! Ravi de vous parler. Comment puis-je vous aider aujourd'hui?",
            "Salut! Je suis là pour vous assister. Que puis-je faire pour vous?",
            "Hello! Content de vous voir. En quoi puis-je vous être utile?",
            "Bonjour! J'espère que vous passez une bonne journée. Comment puis-je vous aider?"
        ]
    },
    "goodbye": {
        "patterns": ["au revoir", "bye", "à bientôt", "salut", "ciao", "adieu"],
        "responses": [
            "Au revoir! N'hésitez pas à revenir si vous avez d'autres questions. 👋",
            "À bientôt! Ce fut un plaisir de vous aider.",
            "Au revoir! Prenez soin de vous et revenez quand vous voulez!",
            "Bye! J'espère avoir été utile. À la prochaine!"
        ]
    },
    "thanks": {
        "patterns": ["merci", "thanks", "thank you", "thx", "merci beaucoup"],
        "responses": [
            "De rien! C'est toujours un plaisir d'aider. 😊",
            "Avec plaisir! N'hésitez pas si vous avez d'autres questions.",
            "Je vous en prie! Content d'avoir pu vous aider.",
            "Pas de quoi! Je suis là pour ça."
        ]
    },
    "identity": {
        "patterns": ["qui es-tu", "qui es tu", "ton nom", "tu es qui", "c'est quoi ton nom", "quel est ton nom"],
        "responses": [
            "Je suis un assistant virtuel intelligent créé avec FastAPI et Python. Mon but est de vous aider et de répondre à vos questions!",
            "Je suis votre chatbot personnel, propulsé par FastAPI. Je peux discuter, répondre à vos questions et vous assister dans diverses tâches.",
            "Je suis un chatbot IA développé pour vous accompagner. Je combine technologie moderne et conversational design!"
        ]
    },
    "capability": {
        "patterns": ["que peux-tu faire", "tes capacités", "tu peux faire quoi", "aide", "help", "comment tu peux m'aider"],
        "responses": [
            "Je peux discuter avec vous, répondre à vos questions, vous donner l'heure, faire des calculs, et bien plus! Essayez de me poser une question.",
            "Mes capacités incluent: répondre à vos questions, faire des calculs mathématiques, vous donner l'heure et la date, et engager des conversations intéressantes.",
            "Je suis là pour vous aider de nombreuses façons! Je peux discuter, calculer, informer, et vous assister dans vos tâches quotidiennes."
        ]
    },
    "mood": {
        "patterns": ["comment vas-tu", "ça va", "comment tu vas", "tu vas bien"],
        "responses": [
            "Je vais très bien, merci de demander! Et vous, comment allez-vous? 😊",
            "Super bien! Je suis toujours prêt à aider. Et vous?",
            "Je vais à merveille! Heureux d'être à votre service. Et vous, ça va?",
            "Excellent! Je suis en pleine forme virtuelle. Comment vous sentez-vous?"
        ]
    },
    "jokes": {
        "patterns": ["blague", "joke", "fais-moi rire", "raconte une blague", "drôle"],
        "responses": [
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant? Parce que sinon ils tombent dans le bateau! 😄",
            "Qu'est-ce qu'un crocodile qui surveille la pharmacie? Un Lacoste garde! 🐊",
            "Qu'est-ce qu'un ordinateur mange au déjeuner? Des micro-chips! 💻",
            "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël? Un chat-peint de Noël! 🎄"
        ]
    }
}

# Mots-clés pour l'analyse de sentiment
sentiment_keywords = {
    "positive": ["super", "génial", "excellent", "parfait", "merveilleux", "formidable", "top", "cool", "bien", "content", "heureux", "joie"],
    "negative": ["mal", "nul", "mauvais", "horrible", "triste", "déçu", "problème", "erreur", "bug", "frustré", "énervé"],
    "neutral": ["ok", "moyen", "normal", "standard", "ordinaire"]
}

def analyze_sentiment(message: str) -> str:
    """Analyse le sentiment d'un message"""
    message_lower = message.lower()
    
    positive_count = sum(1 for word in sentiment_keywords["positive"] if word in message_lower)
    negative_count = sum(1 for word in sentiment_keywords["negative"] if word in message_lower)
    
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

def extract_numbers(text: str) -> List[float]:
    """Extrait les nombres d'un texte"""
    numbers = re.findall(r'-?\d+\.?\d*', text)
    return [float(n) for n in numbers]

def calculate_math(message: str) -> Optional[str]:
    """Effectue des calculs mathématiques simples"""
    message_lower = message.lower()
    numbers = extract_numbers(message)
    
    if len(numbers) < 2:
        return None
    
    # Addition
    if any(word in message_lower for word in ["plus", "+", "additionne", "somme"]):
        result = sum(numbers)
        return f"Le résultat de l'addition est: {result}"
    
    # Soustraction
    if any(word in message_lower for word in ["moins", "-", "soustrait", "différence"]):
        result = numbers[0] - numbers[1]
        return f"Le résultat de la soustraction est: {result}"
    
    # Multiplication
    if any(word in message_lower for word in ["fois", "*", "×", "multiplié", "multiplie", "produit"]):
        result = numbers[0] * numbers[1]
        return f"Le résultat de la multiplication est: {result}"
    
    # Division
    if any(word in message_lower for word in ["divisé", "divise", "/", "÷", "division"]):
        if numbers[1] != 0:
            result = numbers[0] / numbers[1]
            return f"Le résultat de la division est: {result:.2f}"
        else:
            return "Impossible de diviser par zéro!"
    
    # Puissance
    if any(word in message_lower for word in ["puissance", "exposant", "^", "**"]):
        result = numbers[0] ** numbers[1]
        return f"Le résultat est: {result}"
    
    return None

def get_contextual_response(message: str, conversation_history: List[Dict]) -> Optional[str]:
    """Génère des réponses contextuelles basées sur l'historique"""
    message_lower = message.lower()
    
    # Référence à des messages précédents
    if any(word in message_lower for word in ["précédent", "avant", "dernier message", "disais"]):
        if len(conversation_history) >= 2:
            last_bot_message = None
            for msg in reversed(conversation_history[:-1]):
                if msg["role"] == "assistant":
                    last_bot_message = msg["content"]
                    break
            if last_bot_message:
                return f"J'ai dit: '{last_bot_message}'. Voulez-vous en savoir plus?"
    
    # Demande de répétition
    if any(word in message_lower for word in ["répète", "redis", "encore", "quoi"]) and len(conversation_history) >= 2:
        last_bot_message = None
        for msg in reversed(conversation_history[:-1]):
            if msg["role"] == "assistant":
                last_bot_message = msg["content"]
                break
        if last_bot_message:
            return f"Je répète: {last_bot_message}"
    
    return None

def generate_ai_response(user_message: str, conversation_history: List[Dict]) -> Optional[str]:
    """Génère une réponse en utilisant l'API IA"""
    if not ai_client or AI_PROVIDER == "local":
        return None
    
    try:
        # Préparer les messages pour l'IA
        messages = [
            {
                "role": "system",
                "content": "Tu es un assistant virtuel intelligent, amical et serviable. Tu réponds en français de manière claire et concise. Tu peux aider avec diverses tâches, répondre aux questions et avoir des conversations naturelles."
            }
        ]
        
        # Ajouter l'historique de conversation (limité aux 10 derniers messages)
        for msg in conversation_history[-10:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Ajouter le message actuel
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Appeler l'API selon le provider
        if AI_PROVIDER == "groq":
            completion = ai_client.chat.completions.create(
                model=AI_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
                top_p=1,
                stream=False
            )
        elif AI_PROVIDER == "openai":
            completion = ai_client.chat.completions.create(
                model=AI_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
        else:
            return None
        
        return completion.choices[0].message.content
    
    except Exception as e:
        print(f"❌ Erreur IA: {e}")
        return None

def generate_response(user_message: str, conversation_id: str = None) -> str:
    """Génère une réponse intelligente basée sur le message de l'utilisateur"""
    user_message_lower = user_message.lower().strip()
    
    # Récupérer l'historique de conversation
    conversation_history = conversations.get(conversation_id, []) if conversation_id else []
    
    # Analyse de sentiment
    sentiment = analyze_sentiment(user_message)
    
    # Réponse contextuelle basée sur l'historique
    contextual_response = get_contextual_response(user_message, conversation_history)
    if contextual_response:
        return contextual_response
    
    # Calculs mathématiques
    math_result = calculate_math(user_message)
    if math_result:
        return math_result
    
    # Questions sur le temps (priorité haute)
    if any(word in user_message_lower for word in ["heure", "time", "quelle heure"]):
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Il est actuellement {current_time}. ⏰"
    
    if any(word in user_message_lower for word in ["date", "jour", "aujourd'hui", "quel jour"]):
        current_date = datetime.now().strftime("%d/%m/%Y")
        day_name = datetime.now().strftime("%A")
        days_fr = {
            "Monday": "lundi", "Tuesday": "mardi", "Wednesday": "mercredi",
            "Thursday": "jeudi", "Friday": "vendredi", "Saturday": "samedi", "Sunday": "dimanche"
        }
        return f"Nous sommes le {days_fr.get(day_name, day_name)} {current_date}. 📅"
    
    # Essayer d'utiliser l'IA externe d'abord
    if AI_PROVIDER != "local":
        ai_response = generate_ai_response(user_message, conversation_history)
        if ai_response:
            return ai_response
    
    # Recherche dans la base de connaissances locale (fallback)
    for category, data in knowledge_base.items():
        for pattern in data["patterns"]:
            if pattern in user_message_lower:
                response = random.choice(data["responses"])
                # Ajouter une touche basée sur le sentiment
                if sentiment == "positive":
                    response += " Vous semblez de bonne humeur! 😊"
                return response
    
    # Réponses intelligentes basées sur le type de message
    if "?" in user_message:
        questions_responses = [
            f"C'est une excellente question! Pour répondre à '{user_message}', j'aurais besoin de plus de contexte. Pouvez-vous préciser?",
            f"Intéressant comme question! Je réfléchis à '{user_message}'. Pouvez-vous me donner plus de détails?",
            f"Belle question! Concernant '{user_message}', pourriez-vous être plus spécifique pour que je puisse mieux vous aider?"
        ]
        return random.choice(questions_responses)
    
    # Détection de programmation
    if any(word in user_message_lower for word in ["python", "code", "programmation", "développement", "fastapi", "api"]):
        return "Ah, un passionné de programmation! Python et FastAPI sont d'excellents choix. Comment puis-je vous aider avec votre projet de développement? 💻"
    
    # Réponses basées sur le sentiment
    if sentiment == "negative":
        return "Je sens que quelque chose ne va pas. Comment puis-je vous aider à résoudre ce problème? Je suis là pour vous assister. 🤝"
    
    if sentiment == "positive":
        return "C'est génial! Votre enthousiasme est contagieux! Comment puis-je contribuer à votre bonne humeur? 😄"
    
    # Réponses variées par défaut
    default_responses = [
        f"Intéressant! Vous dites '{user_message}'. Pouvez-vous m'en dire plus?",
        f"J'ai bien noté: '{user_message}'. Comment puis-je vous aider avec cela?",
        f"Merci pour ce message. Concernant '{user_message}', que souhaitez-vous savoir exactement?",
        "Je comprends ce que vous dites. Voulez-vous que je développe sur un aspect particulier?",
        "C'est noté! Y a-t-il quelque chose de spécifique que vous aimeriez que je fasse?"
    ]
    
    return random.choice(default_responses)

@app.get("/")
async def root():
    """Page d'accueil - retourne l'interface HTML"""
    return FileResponse("static/index.html")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Endpoint principal pour le chat"""
    try:
        # Générer un ID de conversation si nécessaire
        conversation_id = request.conversation_id or f"conv_{datetime.now().timestamp()}"
        
        # Initialiser la conversation si elle n'existe pas
        if conversation_id not in conversations:
            conversations[conversation_id] = []
        
        # Ajouter le message de l'utilisateur
        user_message = Message(
            role="user",
            content=request.message,
            timestamp=datetime.now().isoformat()
        )
        conversations[conversation_id].append(user_message.dict())
        
        # Générer la réponse avec le contexte de conversation
        bot_response_text = generate_response(request.message, conversation_id)
        
        # Ajouter la réponse du bot
        bot_message = Message(
            role="assistant",
            content=bot_response_text,
            timestamp=datetime.now().isoformat()
        )
        conversations[conversation_id].append(bot_message.dict())
        
        return ChatResponse(
            response=bot_response_text,
            conversation_id=conversation_id,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/conversation/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Récupère l'historique d'une conversation"""
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation non trouvée")
    
    return {"conversation_id": conversation_id, "messages": conversations[conversation_id]}

@app.delete("/api/conversation/{conversation_id}")
async def delete_conversation(conversation_id: str):
    """Supprime une conversation"""
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation non trouvée")
    
    del conversations[conversation_id]
    return {"message": "Conversation supprimée avec succès"}

@app.get("/api/conversations")
async def list_conversations():
    """Liste toutes les conversations"""
    return {
        "total": len(conversations),
        "conversations": [
            {
                "id": conv_id,
                "message_count": len(messages),
                "last_message": messages[-1]["timestamp"] if messages else None
            }
            for conv_id, messages in conversations.items()
        ]
    }

@app.get("/health")
async def health_check():
    """Endpoint de santé"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Monter le dossier static
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except:
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
