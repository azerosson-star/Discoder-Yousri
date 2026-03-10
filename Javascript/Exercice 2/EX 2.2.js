conteneur = document.getElementById('conteneur');
boite = document.getElementById('boite');
 btn = document.getElementById('btn');

conteneur.addEventListener('click', () => {
    console.log("Conteneur");
});

boite.addEventListener('click', () => {
    console.log("Boite");
});

btn.addEventListener('click', (e) => {
    e.stopPropagation();
    console.log("Bouton");
});