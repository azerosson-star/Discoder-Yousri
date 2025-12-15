import sqlite3
from flask import Flask
app = Flask (__name__)
from flask import request, render_template

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        # C'est ici qu'on récupère les données du formulaire
        # Disons que tes champs HTML ont name="pseudo" et name="password"
        
    
        valeur_pseudo = request.form['username']
        valeur_mdp = request.form['password']

        # 1. On se connecte à la base de données
        conn = sqlite3.connect('../BDD/BDD.db')
        cursor = conn.cursor()

        # 2. On vérifie si ce duo (username + pwd) existe dans la table Users
        cursor.execute("SELECT * FROM Users WHERE username = ? AND pwd = ?", (valeur_pseudo, valeur_mdp))
        utilisateur = cursor.fetchone()

        # 3. On ferme la connexion (c'est important !)
        conn.close()

        # 4. On décide quoi afficher
        if utilisateur:
            return "Connexion réussie ! Bienvenue " + valeur_pseudo
        else:
            return "Erreur : Identifiant ou mot de passe incorrect."