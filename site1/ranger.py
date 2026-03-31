import os
import shutil

# L'architecture cible selon votre tableau blanc
fichiers_cibles = {
    'Nav.Class.php': 'php/controller/classes/Nav.Class.php',
    'contact.php': 'php/view/form/contact.php',
    'head.php': 'php/view/general/head.php',
    'header.php': 'php/view/general/header.php',
    'footer.php': 'php/view/general/footer.php',
    'accueil.php': 'php/view/general/accueil.php',
    'produits.php': 'php/view/list/produits.php',
}

# Fonction pour trouver un fichier, peu importe où il est caché dans le dossier
def trouver_fichier(nom_fichier, chemin_recherche="."):
    for racine, dossiers, fichiers in os.walk(chemin_recherche):
        if nom_fichier in fichiers:
            return os.path.join(racine, nom_fichier)
    return None

print("--- Reorganisation MVC selon le tableau blanc ---")

for nom_fichier, destination in fichiers_cibles.items():
    source = trouver_fichier(nom_fichier)
    
    if source:
        # On vérifie si le fichier n'est pas déjà au bon endroit
        if os.path.abspath(source) == os.path.abspath(destination):
            print(f"[INFO] {nom_fichier} est deja a sa place : {destination}")
            continue
            
        # Création du dossier cible s'il n'existe pas
        dossier_parent = os.path.dirname(destination)
        if dossier_parent and not os.path.exists(dossier_parent):
            os.makedirs(dossier_parent, exist_ok=True)
            
        # Déplacement
        try:
            shutil.move(source, destination)
            print(f"[OK] Deplace : {source} -> {destination}")
        except Exception as e:
            print(f"[ERREUR] Impossible de deplacer {nom_fichier} : {e}")
    else:
        print(f"[ATTENTION] Fichier introuvable : {nom_fichier}")

print("\nTermine ! N'oubliez pas de mettre a jour index.php.")