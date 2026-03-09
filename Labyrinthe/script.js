// Récupération de l'élément du joueur (le carré rouge)
let monCarre = document.getElementById("joueur");

// Lecture de la position initiale du joueur définie dans le CSS
// Cela évite un bug de téléportation au premier mouvement
let positionX = monCarre.offsetLeft;
let positionY = monCarre.offsetTop;

// Fonction principale pour déplacer le joueur
// Paramètres : horizontal (déplacement en X), vertical (déplacement en Y)
function faireBouger(horizontal, vertical) {
    // Mise à jour des coordonnées
    positionX = positionX + horizontal;
    positionY = positionY + vertical;

    // Application du déplacement à l'élément HTML
    monCarre.style.left = positionX + "px";
    monCarre.style.top = positionY + "px";
}

// Gestion des boutons de contrôle
document.getElementById("btnHaut").addEventListener("click", function() {
    faireBouger(0, -5); // Déplacement vers le haut
});

document.getElementById("btnBas").addEventListener("click", function() {
    faireBouger(0, 5); // Déplacement vers le bas
});

document.getElementById("btnGauche").addEventListener("click", function() {
    faireBouger(-5, 0); // Déplacement vers la gauche
});

document.getElementById("btnDroite").addEventListener("click", function() {
    faireBouger(5, 0); // Déplacement vers la droite
});

// Gestion du clavier pour les flèches directionnelles
document.addEventListener("keydown", function(event) {
    if (event.key == "ArrowUp") {
        faireBouger(0, -5); // Flèche Haut
    }
    else if (event.key == "ArrowDown") {
        faireBouger(0, 5); // Flèche Bas
    }
    else if (event.key == "ArrowLeft") {
        faireBouger(-5, 0); // Flèche Gauche
    }
    else if (event.key == "ArrowRight") {
        faireBouger(5, 0); // Flèche Droite
    }
});