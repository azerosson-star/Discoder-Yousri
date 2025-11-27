const leFormulaire = document.getElementById("formulaire");
leFormulaire.addEventListener("submit", function(event) 
{
    event.preventDefault(); // On bloque le rechargement

    // On récupère les valeurs AVEC les bons IDs et .value
    const email = document.getElementById("e-mail").value;
    const password = document.getElementById("mdp").value;

    // On affiche le résultat
    alert("Email : " + email + "\nMot de passe : " + password);
});
