nom = getElementById("name")
prenom = getElementById("prenom")
mail = getElementById("mail")
date = getElementById("date")
date2 = getElementById("date2")
cp = getElementById("cp")
tel = getElementById("tel")
mpd = getElementById("mpd")

nom.addeventlistener("change",verifNom) //addEventListener

function verifNom(){
    if(nom.value.length < 2){
        alert("Le nom doit contenir au moins 2 caractères")
    }
}

prenom.addeventlistener("change",verifPrenom)  //addEventListener

function verifPrenom(){
    if(prenom.value.length < 2){
        alert("Le prénom doit contenir au moins 2 caractères")
    }
}