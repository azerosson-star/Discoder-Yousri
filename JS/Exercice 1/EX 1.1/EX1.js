// On sélectionne la div "Bonjour", le formulaire et le champ de texte
monboutton = document.querySelector('.OK');
monFormulaire = document.querySelector('.formulaire');
champPrenom = document.querySelector('.champ-prenom');

// On écoute le clic sur le texte "Bonjour"
monboutton.addEventListener('click', () => {
    
    // On récupère ce que l'utilisateur a tapé dans la case
    let prenomTape = champPrenom.value;
    
    if (prenomTape !== "") {
        alert("Bonjour "+ prenomTape);
    } else {
        alert("Veuillez d'abord entrer un prénom !");
    }
});