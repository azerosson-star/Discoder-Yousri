"""
Exemples d'utilisation de la base de données SQL
Script pour montrer comment interagir avec la base de données
"""
import asyncio
from database import AsyncSessionLocal
import crud


async def example_create_conversation():
    """Exemple 1: Créer une nouvelle conversation"""
    print("\n📝 Exemple 1: Créer une conversation")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        # Créer une conversation
        conv = await crud.create_conversation(db, user_name="Jean Dupont")
        print(f"✅ Conversation créée:")
        print(f"   ID: {conv.conversation_id}")
        print(f"   Utilisateur: {conv.user_name}")
        print(f"   Créée le: {conv.created_at}")
        
        return conv.conversation_id


async def example_add_messages(conv_id: str):
    """Exemple 2: Ajouter des messages"""
    print("\n💬 Exemple 2: Ajouter des messages")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        # Message utilisateur
        msg1 = await crud.create_message(
            db, conv_id, "user", "Quel temps fait-il aujourd'hui?"
        )
        print(f"✅ Message utilisateur ajouté (ID: {msg1.id})")
        
        # Réponse assistant
        msg2 = await crud.create_message(
            db, conv_id, "assistant", "Il fait beau et ensoleillé! Température: 22°C"
        )
        print(f"✅ Message assistant ajouté (ID: {msg2.id})")


async def example_get_conversation(conv_id: str):
    """Exemple 3: Récupérer une conversation avec tous ses messages"""
    print("\n📖 Exemple 3: Récupérer une conversation")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        conv = await crud.get_conversation(db, conv_id)
        
        if conv:
            print(f"✅ Conversation trouvée:")
            print(f"   ID: {conv.conversation_id}")
            print(f"   Utilisateur: {conv.user_name}")
            print(f"   Nombre de messages: {len(conv.messages)}")
            print("\n   Messages:")
            
            for i, msg in enumerate(conv.messages, 1):
                print(f"   {i}. [{msg.role}] {msg.content}")
                print(f"      Timestamp: {msg.timestamp}")
        else:
            print("❌ Conversation non trouvée")


async def example_list_all_conversations():
    """Exemple 4: Lister toutes les conversations"""
    print("\n📋 Exemple 4: Lister toutes les conversations")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        conversations = await crud.get_conversations(db, skip=0, limit=10)
        
        print(f"✅ {len(conversations)} conversation(s) trouvée(s):\n")
        
        for i, conv in enumerate(conversations, 1):
            msg_count = await crud.get_message_count(db, conv.id)
            print(f"{i}. Conversation: {conv.conversation_id[:20]}...")
            print(f"   Utilisateur: {conv.user_name or 'Anonyme'}")
            print(f"   Messages: {msg_count}")
            print(f"   Dernière activité: {conv.updated_at}")
            print()


async def example_get_stats():
    """Exemple 5: Obtenir les statistiques"""
    print("\n📊 Exemple 5: Statistiques")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        stats = await crud.get_conversation_stats(db)
        
        print(f"✅ Statistiques globales:")
        print(f"   Total de conversations: {stats['total_conversations']}")
        print(f"   Total de messages: {stats['total_messages']}")
        print(f"   Moyenne de messages par conversation: {stats['average_messages_per_conversation']:.2f}")


async def example_user_context(conv_id: str):
    """Exemple 6: Gérer le contexte utilisateur"""
    print("\n👤 Exemple 6: Contexte utilisateur")
    print("-" * 50)
    
    async with AsyncSessionLocal() as db:
        # Créer/mettre à jour le contexte
        import json
        preferences = json.dumps({
            "language": "fr",
            "theme": "dark",
            "notifications": True
        })
        
        context = await crud.create_or_update_user_context(
            db, conv_id, 
            user_name="Jean Dupont",
            preferences=preferences
        )
        
        print(f"✅ Contexte utilisateur créé/mis à jour:")
        print(f"   ID: {context.id}")
        print(f"   Conversation: {context.conversation_id}")
        print(f"   Utilisateur: {context.user_name}")
        print(f"   Préférences: {context.preferences}")


async def example_delete_conversation(conv_id: str):
    """Exemple 7: Supprimer une conversation"""
    print("\n🗑️  Exemple 7: Supprimer une conversation")
    print("-" * 50)
    
    # Demander confirmation
    print(f"⚠️  Voulez-vous vraiment supprimer la conversation {conv_id[:20]}...?")
    print("   (Cette opération supprimera aussi tous les messages)")
    
    # Pour la démo, on commente la suppression
    print("   [DEMO] Suppression commentée pour préserver les données")
    
    # Pour vraiment supprimer, décommenter:
    # async with AsyncSessionLocal() as db:
    #     deleted = await crud.delete_conversation(db, conv_id)
    #     if deleted:
    #         print(f"✅ Conversation supprimée avec succès")
    #     else:
    #         print(f"❌ Conversation non trouvée")


async def example_search_messages():
    """Exemple 8: Rechercher dans les messages (requête personnalisée)"""
    print("\n🔍 Exemple 8: Recherche personnalisée")
    print("-" * 50)
    
    from sqlalchemy import select
    from models import Message
    
    async with AsyncSessionLocal() as db:
        # Rechercher tous les messages contenant "temps"
        result = await db.execute(
            select(Message)
            .where(Message.content.contains("temps"))
            .limit(5)
        )
        messages = result.scalars().all()
        
        print(f"✅ {len(messages)} message(s) trouvé(s) contenant 'temps':\n")
        
        for msg in messages:
            print(f"   [{msg.role}] {msg.content}")
            print(f"   Timestamp: {msg.timestamp}")
            print()


async def run_all_examples():
    """Exécuter tous les exemples"""
    print("\n" + "=" * 60)
    print("🎓 EXEMPLES D'UTILISATION DE LA BASE DE DONNÉES SQL")
    print("=" * 60)
    
    # Exemple 1: Créer une conversation
    conv_id = await example_create_conversation()
    
    # Exemple 2: Ajouter des messages
    await example_add_messages(conv_id)
    
    # Exemple 3: Récupérer la conversation
    await example_get_conversation(conv_id)
    
    # Exemple 4: Lister toutes les conversations
    await example_list_all_conversations()
    
    # Exemple 5: Statistiques
    await example_get_stats()
    
    # Exemple 6: Contexte utilisateur
    await example_user_context(conv_id)
    
    # Exemple 7: Suppression (démo)
    await example_delete_conversation(conv_id)
    
    # Exemple 8: Recherche
    await example_search_messages()
    
    print("\n" + "=" * 60)
    print("✨ Tous les exemples ont été exécutés avec succès!")
    print("=" * 60)
    print("\n💡 Conseil: Utilisez ces exemples comme base pour vos")
    print("   propres fonctionnalités personnalisées!")


if __name__ == "__main__":
    asyncio.run(run_all_examples())
