liste = document.getElementById('liste');
info = document.getElementById('info');

liste.addEventListener('click', function(e) {
    if (e.target.classList.contains('suppr')) {
         liASupprimer = e.target.closest('li');
        if (liASupprimer) {
            liASupprimer.remove();
        }
    } else {
        liCible = e.target.closest('li');
        if (liCible) {
            document.querySelectorAll('#liste li').forEach(li => li.classList.remove('selectionne'));
            liCible.classList.add('selectionne');
            info.textContent = `ID sélectionné : ${liCible.dataset.id}`;
        }
    }
});