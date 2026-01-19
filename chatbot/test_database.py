"""
Script de test pour vérifier la connexion à la base de données
"""
import asyncio
from sqlalchemy import text
from database import engine, create_tables, drop_tables
from crud import (
    create_conversation,
    create_message,
    get_conversation,
    get_conversations,
    get_conversation_stats
)


async def test_database():
    """Test complet de la base de données"""
    
    print("🧪 Test de la base de données SQL")
    print("=" * 60)
    
    # Étape 1: Créer les tables
    print("\n1️⃣ Création des tables...")
    await create_tables()
    print("   ✅ Tables créées avec succès")
    
    # Étape 2: Tester la connexion
    print("\n2️⃣ Test de connexion...")
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(f"   ✅ Connexion réussie: {result.scalar()}")
    
    # Étape 3: Importer la session
    from database import AsyncSessionLocal
    
    # Étape 4: Créer une conversation de test
    print("\n3️⃣ Création d'une conversation de test...")
    async with AsyncSessionLocal() as session:
        conversation = await create_conversation(session, user_name="Test User")
        print(f"   ✅ Conversation créée: {conversation.conversation_id}")
        conv_id = conversation.conversation_id
    
    # Étape 5: Ajouter des messages
    print("\n4️⃣ Ajout de messages...")
    async with AsyncSessionLocal() as session:
        msg1 = await create_message(
            session,
            conversation_id=conv_id,
            role="user",
            content="Bonjour, comment ça va?"
        )
        print(f"   ✅ Message utilisateur créé (ID: {msg1.id})")
        
        msg2 = await create_message(
            session,
            conversation_id=conv_id,
            role="assistant",
            content="Bonjour! Je vais très bien, merci!"
        )
        print(f"   ✅ Message assistant créé (ID: {msg2.id})")
    
    # Étape 6: Récupérer la conversation
    print("\n5️⃣ Récupération de la conversation...")
    async with AsyncSessionLocal() as session:
        conv = await get_conversation(session, conv_id)
        if conv:
            print(f"   ✅ Conversation récupérée: {len(conv.messages)} messages")
            
            for i, msg in enumerate(conv.messages, 1):
                print(f"      {i}. [{msg.role}] {msg.content[:50]}...")
        else:
            print("   ❌ Conversation non trouvée.")
    
    # Étape 7: Statistiques
    print("\n6️⃣ Statistiques...")
    async with AsyncSessionLocal() as session:
        stats = await get_conversation_stats(session)
        print(f"   ✅ Total conversations: {stats['total_conversations']}")
        print(f"   ✅ Total messages: {stats['total_messages']}")
        print(f"   ✅ Moyenne messages/conv: {stats['average_messages_per_conversation']:.2f}")
    
    # Étape 8: Liste des conversations
    print("\n7️⃣ Liste des conversations...")
    async with AsyncSessionLocal() as session:
        conversations = await get_conversations(session)
        print(f"   ✅ {len(conversations)} conversation(s) trouvée(s)")
    
    print("\n" + "=" * 60)
    print("✨ Tous les tests sont passés avec succès!")
    print("\n📊 Base de données SQLite créée: chatbot.db")
    print("🚀 Vous pouvez maintenant lancer: python main.py")

    # Arrêt propre (évite des threads résiduels à la fermeture de l'interpréteur)
    try:
        await engine.dispose()
    except Exception:
        pass


async def reset_database():
    """Réinitialise complètement la base de données"""
    print("\n⚠️  Réinitialisation de la base de données...")
    await drop_tables()
    print("   ✅ Tables supprimées")
    await create_tables()
    print("   ✅ Tables recréées")


if __name__ == "__main__":
    # Lancer les tests
    try:
        asyncio.run(test_database())
    except Exception as e:
        print(f"\n❌ Erreur lors des tests: {e}")
        import traceback
        traceback.print_exc()
