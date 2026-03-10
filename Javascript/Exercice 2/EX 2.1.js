const saisie = document.getElementById('saisie');
const affichage = document.getElementById('affichage');

saisie.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        saisie.value = '';
        affichage.textContent = "Champ réinitialisé";
    } else {
        setTimeout(() => {
            affichage.textContent = `Touche pressée : ${e.key} | Valeur actuelle : ${saisie.value}`;
        }, 0);
    }
});
