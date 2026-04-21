villes = ["Valenciennes", "Denain", "Nantes"];
    
villes.forEach(function(ville) {

    requete = new XMLHttpRequest();
    lien = 'https://api.weatherapi.com/v1/forecast.json?key=064012d2ca954542948141920262004&q=' + ville;
    requete.open('GET', lien);     

    requete.send();
    requete.onreadystatechange = function(event) {
        if (this.readyState == XMLHttpRequest.DONE) {
            if (this.status === 200) {
                contenu = JSON.parse(this.responseText);
                zone = document.getElementById("resultats");
                zone.innerHTML += "<p>" + ville + " : " + contenu.current.temp_c + "°C</p>";
            }
        }
    }

});