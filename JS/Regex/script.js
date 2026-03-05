lesinput = document.querySelectorAll("input");

lesinput.forEach(element => {
    element.addEventListener("change", regex);
});

function regex(e) {
     cible = e.target;
    if(!cible.checkValidity()==true) {
        cible.classList.remove("valid");
        cible.classList.add("erreur");
    } else {
        cible.classList.remove("erreur");
        cible.classList.add("valid");
    }
}


mdp = document.getElementById("mdp");

mdp.addEventListener("input",regexMdp);
function regexMdp(e) {
     valeur = e.target.value;
maj = document.querySelector("#maj")
min = document.querySelector("#min")
num = document.querySelector("#num")
long = document.querySelector("#long")


    
    if (/[A-Z]/.test(valeur)) {
        maj.textContent = "✔️ Une majuscule";
        maj.style.color = "green";
} else{
       maj.textContent = "❌ Une majuscule";
        maj.style.color = "red";
    
}

      if (/[a-z]/.test(valeur)) {
        min.textContent = "✔️ Une minuscule";
        min.style.color = "green";
} else{
       min.textContent = "❌ Une minuscule";
        min.style.color = "red";
    
}
    
    if (/[0-9]/.test(valeur)) {
        num.textContent = "✔️ Un chiffre";
        num.style.color = "green";
} else{
       num.textContent = "❌ Un chiffre";
        num.style.color = "red";
    
}    
    if (/{8,}/.test(valeur)) {
        long.textContent = "✔️ Au moins 8 caractères";
        long.style.color = "green";
} else{
       long.textContent = "❌ Au moins 8 caractères";
        long.style.color = "red";
    
}}
