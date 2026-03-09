/**
 * =========================================
 * JEU DE MÉMOIRE - SCRIPT PRINCIPAL
 * =========================================
 * Ce script gère un jeu de mémoire où le joueur
 * doit trouver les paires de cartes identiques.
 */

// --- VARIABLES GLOBALES (ÉTAT DU JEU) ---

/**
 * @type {Element|null}
 * Stocke la première carte cliquée par le joueur
 * Sera utilisée pour comparer avec la deuxième carte
 */
let clic1 = null;     

/**
 * @type {Element|null}
 * Stocke la deuxième carte cliquée par le joueur
 * Sera comparée avec la première carte (clic1)
 */
let clic2 = null; 

/**
 * @type {boolean}
 * Bloquer les clics pendant qu'on attend la comparaison
 * Empêche le joueur de cliquer trop rapidement
 * ou de cliquer plus de 2 cartes à la fois
 */
let bloqueClic = false;    

/**
 * @type {number}
 * Compteur du nombre de paires trouvées correctement
 * Quand on atteint 8 paires, le joueur a gagné
 */
let pairesTrouvees = 0; 

/**
 * @type {number}
 * Compteur du nombre total de clics effectués
 * Sert à afficher le score du joueur
 */
let nombreClics = 0;

/**
 * Sélectionne TOUTES les cartes du jeu (éléments avec la classe "carte")
 * querySelectorAll retourne une NodeList de tous les éléments correspondants
 */
let toutesLesCartes = document.querySelectorAll(".carte");


/**
 * =========================================
 * INITIALISATION DES CARTES
 * =========================================
 * Cette boucle prépare chaque carte pour le jeu:
 * 1. Les mélange aléatoirement
 * 2. Ajoute un écouteur d'événement pour les clics
 */
toutesLesCartes.forEach(function(carte) {
    
    /**
     * Mélange les cartes: attribue un ordre CSS aléatoire
     * Math.random() génère un nombre entre 0 et 1
     * Multiplié par 100 = nombre entre 0 et 100
     * Math.round() arrondit ce nombre à l'entier le plus proche
     * Cette propriété "order" réorganise visuellement les cartes via Flexbox
     */
    carte.style.order = Math.round(Math.random() * 100);
    
    /**
     * Ajoute un écouteur de clic sur chaque carte
     * Quand on clique sur une carte, la fonction "gererClic" est appelée
     * Le paramètre "carte" est passé pour savoir quelle carte a été cliquée
     */
    carte.addEventListener("click", function() {
        gererClic(carte); 
    });
});




/**
 * =========================================
 * FONCTION: GERER UN CLIC SUR UNE CARTE
 * =========================================
 * Cette fonction est appelée chaque fois que le joueur clique sur une carte.
 * Elle gère l'affichage de la carte et la logique du jeu.
 * 
 * @param {Element} carte - L'élément HTML de la carte cliquée
 */
function gererClic(carte) {
    /**
     * CONDITION DE GARDE (GUARD CLAUSE)
     * Vérifier si on PEUT cliquer sur cette carte:
     * 1. bloqueClic == true: Les clics sont actuellement bloqués (en train de comparer)
     * 2. carte.dataset.etat == "affichee": La carte est déjà affichée (impossible de la cliquer à nouveau)
     * 
     * Si l'une de ces conditions est vraie, on sort de la fonction immédiatement
     * avec "return" pour éviter de continuer le traitement
     */
    if (bloqueClic == true || carte.dataset.etat == "affichee") {
        return; 
    }
  
    /**
     * AFFICHAGE DE LA CARTE
     * Change l'image de la carte pour montrer son visage au lieu du dos
     * carte.src = chemin du fichier image stocké dans l'attribut data-imageFace
     * Exemple: "image/Dragon-Blanc-Yeux-Bleus.jpg"
     */
    carte.src = "image/" + carte.dataset.imageFace;
    
    /**
     * MISE À JOUR DE L'ÉTAT DE LA CARTE
     * Marque cette carte comme "affichee" pour qu'on ne puisse plus la cliquer
     * dataset.etat est un attribut data personnalisé HTML5
     */
    carte.dataset.etat = "affichee";

    /**
     * COMPTAGE DES CLICS
     * Augmente le compteur de clics de 1
     * Mises à jour du compteur dans le HTML:
     * L'élément avec id="affichageClics" affiche le nombre total de clics
     */
    nombreClics = nombreClics + 1;
    document.getElementById("affichageClics").innerText = "Clics : " + nombreClics;
    
    /**
     * LOGIQUE DES DEUX CLICS
     * Gération des premières et deuxièmes cartes cliquées
     */
    if (clic1 == null) {
        /**
         * PREMIER CLIC: clic1 n'existe pas encore
         * Donc on enregistre cette première carte cliquée et on attend une deuxième
         */
        clic1 = carte; 
    } else {
        /**
         * DEUXIÈME CLIC: clic1 existe, donc c'est le deuxième clic
         * On enregistre la deuxième carte cliquée
         */
        clic2 = carte;
        
        /**
         * BLOCAGE DES CLICS
         * Empêcher le joueur de cliquer pendant qu'on compare les deux cartes
         * Les clics seront réactivés seulement après la comparaison
         */
        bloqueClic = true;
        
        /**
         * VÉRIFICATION DES PAIRES
         * Appeler la fonction pour vérifier si les deux cartes sont identiques
         */
        verifierPaires(); 
    }
}




/**
 * =========================================
 * FONCTION: VÉRIFIER SI LES DEUX CARTES FORMENT UNE PAIRE
 * =========================================
 * Compare les deux cartes cliquées:
 * - Si elles sont identiques: les garder affichées, incrémenter le score
 * - Si elles sont différentes: les cacher après 1 seconde
 */
function verifierPaires() {
    /**
     * COMPARAISON DES IMAGES
     * Vérifie si les deux cartes ont la même image (même attribut imageFace)
     * clic1.dataset.imageFace et clic2.dataset.imageFace contiennent les noms des images
     * Exemple: "Dragon-Blanc-Yeux-Bleus.jpg" == "Dragon-Blanc-Yeux-Bleus.jpg"
     */
    if (clic1.dataset.imageFace == clic2.dataset.imageFace) {
        /**
         * ✓ LES CARTES SONT IDENTIQUES (PAIRE TROUVÉE!)
         */
        
        /**
         * Augmente le compteur de paires trouvées
         * pairesTrouvees = pairesTrouvees + 1 est équivalent à pairesTrouvees++
         */
        pairesTrouvees = pairesTrouvees + 1;
        
        /**
         * Mise à jour de l'affichage du score dans le HTML
         * L'élément avec id="affichagePaires" affiche le nombre de paires trouvées
         */
        document.getElementById("affichagePaires").innerText = "Paires trouvées : " + pairesTrouvees;
        
        /**
         * RÉINITIALISATION DES VARIABLES
         * Les deux cartes restent affichées (on ne les cache pas)
         * mais on oublie les références clic1 et clic2 pour préparer les prochains clics
         */
        clic1 = null;
        clic2 = null;
        
        /**
         * DÉBLOCAGE DES CLICS
         * Le joueur peut à nouveau cliquer sur d'autres cartes
         */
        bloqueClic = false;
        
        /**
         * VÉRIFICATION DE LA VICTOIRE
         * Il y a 8 paires au total dans ce jeu
         * Si pairesTrouvees == 8, toutes les paires ont été trouvées!
         */
        if (pairesTrouvees == 8) {
            /**
             * Affiche une alerte de victoire avec le nombre de clics utilisés
             * alert() crée une boîte de dialogue popup
             */
            alert("Victoire ! Vous avez fini en " + nombreClics + " clics !");
        }
    } else {
        /**
         * ✗ LES CARTES NE SONT PAS IDENTIQUES (PAIRE NON TROUVÉE)
         * Les cartes doivent être cachées après une courte pause
         */
        
        /**
         * ATTENTE AVANT DE CACHER
         * setTimeout() exécute la fonction "cacherCartes" après 1000 millisecondes (1 seconde)
         * Cela donne au joueur le temps de voir les deux cartes avant qu'elles se cachent
         */
        setTimeout(cacherCartes, 1000);
    }
}




/**
 * =========================================
 * FONCTION: CACHER LES DEUX CARTES
 * =========================================
 * Cette fonction est appelée automatiquement par setTimeout() 
 * si les deux cartes cliquées n'étaient pas une paire.
 * Elle remet les cartes au verso (image du dos) et réinitialise le jeu.
 */
function cacherCartes() {
    /**
     * CACHER LA PREMIÈRE CARTE
     * Remplace l'image de clic1 par l'image du dos (Dos-YGO.jpg)
     * YGO = Yu-Gi-Oh (vraisemblablement le thème des cartes)
     */
    clic1.src = "image/Dos-YGO.jpg";
    
    /**
     * Marque la première carte comme "cachee"
     * Cela permet à gererClic() de savoir qu'on peut la cliquer à nouveau
     */
    clic1.dataset.etat = "cachee";
    
    /**
     * CACHER LA DEUXIÈME CARTE
     * Fait la même chose pour la deuxième carte
     */
    clic2.src = "image/Dos-YGO.jpg";
    clic2.dataset.etat = "cachee";
    
    /**
     * RÉINITIALISATION DES VARIABLES
     * On oublie les références aux deux cartes depuis le jeu principal
     */
    clic1 = null;
    clic2 = null;
    
    /**
     * DÉBLOCAGE DES CLICS
     * Permet au joueur de cliquer à nouveau (la comparaison est terminée)
     */
    bloqueClic = false; 
}


/**
 * =========================================
 * GESTION DES BOUTONS
 * =========================================
 */

/**
 * BOUTON "NOUVELLE PARTIE"
 * Sélectionne le bouton avec id="btnNouvelle" et ajoute un écouteur de clic
 */
document.getElementById("btnNouvelle").addEventListener("click", function() {
    /**
     * location.reload()
     * Recharge la page web entière (FR15)
     * Cela réinitialise toutes les variables, mélange les cartes à nouveau,
     * et le jeu recommence de zéro
     */
    location.reload(); 
});

/**
 * BOUTON "AFFICHER LA SOLUTION"
 * Sélectionne le bouton avec id="btnSolution" et ajoute un écouteur de clic
 */
document.getElementById("btnSolution").addEventListener("click", function() {
    /**
     * AFFICHAGE DE TOUTES LES CARTES
     * Parcourt chaque carte du jeu avec forEach()
     */
    toutesLesCartes.forEach(function(carte) {
        /**
         * Pour chaque carte:
         * 1. Affiche son image (au lieu du dos)
         * 2. Marque son état comme "affichee"
         * 
         * Cela révèle le contenu de TOUTES les cartes simultanément
         * permettant au joueur de voir la solution du puzzle
         */
        carte.src = "image/" + carte.dataset.imageFace;
        carte.dataset.etat = "affichee";
    });
});