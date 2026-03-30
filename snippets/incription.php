<?php


require "inscription_class.php";

$affichageMessage = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nouvelleInscription = new Inscription($_POST);
    $nouvelleInscription->enregistrer();
    $affichageMessage = $nouvelleInscription->getMessage();
}


$form=<<<HTML
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire d'inscription</title>
    <link rel="stylesheet" href="inscription.css">
</head>
<body>
    <main>
        <form action="" method="POST">
            <div class="inscription">
                <h2 style="text-align: center; margin-top: 0; color: #333;">Inscription</h2>

                $affichageMessage

                <div class="groupe">
                    <label for="nom">Nom :</label>
                    <input type="text" id="nom" name="nom" placeholder="Ex: Dupont" autocomplete="family-name" pattern="^[a-zA-ZÀ-ÿ\s\-]+$" title="Seules les lettres sont acceptées." required>
                </div>
                
                <div class="groupe">
                    <label for="prenom">Prénom :</label>
                    <input type="text" id="prenom" name="prenom" placeholder="Ex: Jean" autocomplete="given-name" pattern="^[a-zA-ZÀ-ÿ\s\-]+$" title="Seules les lettres sont acceptées." required>
                </div>
                
                <div class="groupe">
                    <label for="email">E-mail :</label>
                    <input type="email" id="email" name="email" placeholder="jean.dupont@email.com" autocomplete="email" pattern="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$" title="Format attendu : nom@domaine.com" required>
                </div>
                
                <div class="groupe">
                    <label for="mdp">Mot de passe :</label>
                    <div class="input-wrapper">
                        <input type="password" id="mdp" name="mdp" placeholder="••••••••" autocomplete="new-password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Au moins 8 caractères, une majuscule, une minuscule et un chiffre." required>
                        <button type="button" id="toggle-mdp" class="btn-oeil" title="Afficher/Masquer le mot de passe">
                            <svg id="icon-oeil-ouvert" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px; color: #666;">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                            </svg>
                            <svg id="icon-oeil-ferme" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px; color: #666; display: none;">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
                            </svg>
                        </button>
                    </div>
                </div>
                
                <div class="groupe">
                    <label for="date">Date de naissance :</label>
                    <input type="date" id="date" name="date" max="2008-03-30" required>
                </div>
                
                <button type="submit" class="btn-submit">S'inscrire</button>
            </div>
        </form>
    </main>
    <script src="inscription.js"></script>
</body>
</html>
HTML;


echo $form;