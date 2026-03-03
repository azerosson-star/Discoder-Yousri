const monUl = document.querySelector("ul");
const monboutton = document.querySelector("button");
monboutton.addEventListener("click" , () => {
    let reponse = prompt ("Entrer une valeur ou un texte");

    if(reponse != null) {

        let nouveauli = document.createElement("li");

        nouveauli.textContent = reponse;
        monUl.appendChild(nouveauli);
    }
});