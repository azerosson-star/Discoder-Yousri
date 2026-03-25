

    function validerAvecRegex(inputElement, regex) {
         groupeParent = inputElement.parentElement; 
         valeur = inputElement.value.trim(); 

        if (regex.test(valeur)) {
            groupeParent.classList.remove('erreur');
            return true;
        } else {
            groupeParent.classList.add('erreur');
            return false;
        }
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 

         regexNom = /^[a-zA-ZÀ-ÿ\s-]{2,}$/; 
         regexEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/; 

         Nom = document.getElementById('nom');
         Email = document.getElementById('email');
         Personnes = document.getElementById('personnes');
         Date = document.getElementById('date');

        let formulaireValide = true;
        
        if (validerAvecRegex(Nom, regexNom) === false) {
            formulaireValide = false;
        }

        if (validerAvecRegex(Email, regexEmail) === false) {
            formulaireValide = false;
        }
        
         groupePersonnes = Personnes.parentElement;
        if (Personnes.value < 1 || Personnes.value > 15 || Personnes.value === "") {
            groupePersonnes.classList.add('erreur');
            formulaireEstValide = false;
        } else {
            groupePersonnes.classList.remove('erreur');
        }
         
         groupeDate = Date.parentElement;
        if (Date.value === "") {
            groupeDate.classList.add('erreur');
            formulaireEstValide = false;
        } else {
            groupeDate.classList.remove('erreur');
        }
       
        if (formulaireEstValide === true) {
            alert("Merci " + Nom.value + " ! Votre réservation pour " + Personnes.value + " personne(s) le " + Date.value + " est confirmée.");
            form.reset(); 
        }
    });
