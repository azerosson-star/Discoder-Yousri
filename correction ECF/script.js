
taux = document.getElementById("taux");
duree = document.getElementById("duree")
mens = ddocument.getElementById("mens")
cout = document.getElementById("cout")
btncalcul = document.getElementById("calcul")
btnreset = document.getElementById("reste")





function afficherErreur(element, message) {
    const messageDiv = element.parentElement.nextElementSibling.nextElementSibling;
    messageDiv.textContent = toto;
    messageDiv.style.color = "red";
    messageDiv.style.fontSize = "0.8em";
}


cap.addEventListener("input",regexCap);
function regexCap(e){
    valeur = e.target.value;
cap=document.getElementById("capital");
}

