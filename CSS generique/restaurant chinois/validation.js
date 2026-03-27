
    form = document.getElementById('form-reservation');

 
    function validerChampAvecRegex(inputElement, regex) {
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

        // Récupération des champs
         champNom = document.getElementById('nom');
         champEmail = document.getElementById('email');
         champPersonnes = document.getElementById('personnes');
         champDate = document.getElementById('date');

        let formulaireEstValide = true;

        
        if (validerChampAvecRegex(champNom, regexNom) === false) {
            formulaireEstValide = false;
        }

        if (validerChampAvecRegex(champEmail, regexEmail) === false) {
            formulaireEstValide = false;
        }

        
         groupePersonnes = champPersonnes.parentElement;
        if (champPersonnes.value < 1 || champPersonnes.value > 15 || champPersonnes.value === "") {
            groupePersonnes.classList.add('erreur');
            formulaireEstValide = false;
        } else {
            groupePersonnes.classList.remove('erreur');
        }

         
         groupeDate = champDate.parentElement;
        if (champDate.value === "") {
            groupeDate.classList.add('erreur');
            formulaireEstValide = false;
        } else {
            groupeDate.classList.remove('erreur');
        }

       
        if (formulaireEstValide === true) {
            alert("Merci " + champNom.value + " ! Votre réservation pour " + champPersonnes.value + " personne(s) le " + champDate.value + " est confirmée.");
            form.reset(); 
        } else {
            console.log("Erreurs détectées, on bloque la réservation.");
        }
    });
