Readme realisé via IA
====================================================================
DOCUMENTATION TECHNIQUE COMPLÈTE DU PROJET WEB (HTML / CSS / JS)
====================================================================

Ce document détaille ligne par ligne le fonctionnement de l'architecture du projet, divisé en trois piliers : la structure (HTML), l'habillage global et spécifique (CSS), et l'interactivité (JavaScript).

--------------------------------------------------------------------
PARTIE 1 : LA STRUCTURE HTML (index.html)
--------------------------------------------------------------------

1. L'intégration des fichiers CSS externes :
<link rel="stylesheet" href="../gen+root.css">
<link rel="stylesheet" href="../responsive.css">
<link rel="stylesheet" href="formulaire.css">
-> L'attribut "href" indique le chemin du fichier. Le "../" signifie "remonte d'un dossier parent". Cela permet au fichier HTML du restaurant de trouver le CSS générique stocké à la racine du projet. L'ordre est crucial : on charge d'abord le générique, puis le responsive, puis le spécifique (qui aura toujours le dernier mot en cas de conflit).

2. Les balises sémantiques :
<header>, <nav>, <main>, <footer>
-> Au lieu d'utiliser de simples <div> (des boîtes sans sens), on utilise des balises sémantiques. Cela aide les moteurs de recherche (SEO) et les lecteurs d'écran pour malvoyants (Accessibilité) à comprendre la structure de la page.

3. L'attribut "novalidate" du formulaire :
<form id="form-reservation" novalidate>
-> Par défaut, le navigateur web (Chrome, Firefox) possède ses propres bulles d'erreur pour les champs (ex: "Veuillez remplir ce champ"). L'attribut "novalidate" bloque ce comportement natif pour nous laisser le contrôle total des erreurs via notre propre JavaScript.

4. L'organisation des champs (groupe-champ) :
<div class="groupe-champ"> ... <label> ... <input> ... <span class="message-erreur"> </div>
-> Chaque question du formulaire est isolée dans une "div" parente. Cela permet en JavaScript de cibler facilement toute la zone d'une question pour la colorer en rouge d'un seul coup si l'input est faux.

--------------------------------------------------------------------
PARTIE 2 : L'HABILLAGE CSS GÉNÉRIQUE ET RESPONSIVE
--------------------------------------------------------------------

1. La déclaration des variables (Le pseudo-élément :root) :
:root { --couleur-primaire: #4CAF50; }
-> Le ":root" cible la racine absolue du document HTML. Les variables (qui commencent toujours par deux tirets "--") créent un lexique de couleurs réutilisable. Pour les utiliser, on écrit "var(--couleur-primaire)". Si on doit changer le design entier d'un site, on ne modifie que le bloc :root, tout le reste s'adapte automatiquement.

2. Le Reset CSS Universel :
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
-> L'astérisque (*) sélectionne toutes les balises. 
-> "margin: 0; padding: 0;" : Annule les marges aléatoires que les navigateurs appliquent par défaut aux titres ou aux paragraphes.
-> "box-sizing: border-box;" : C'est la règle d'or du CSS moderne. Elle oblige le navigateur à inclure les bordures (border) et les marges intérieures (padding) dans le calcul de la largeur totale d'un élément, évitant ainsi que des boîtes ne débordent de l'écran.

3. Le centrage du site (dans le body) :
max-width: 1200px; margin: 0 auto;
-> "max-width" fixe une largeur limite. Si l'écran fait 2000px de large, le site s'arrêtera à 1200px.
-> "margin: 0 auto;" : Le "0" indique qu'il n'y a pas de marge en haut/bas. Le "auto" demande au navigateur de calculer automatiquement les marges à gauche et à droite de manière égale, ce qui a pour effet de centrer parfaitement le site au milieu de l'écran.

4. La grille (CSS Grid) pour la Navbar :
display: grid; grid-template-columns: 1fr 1fr 1fr 1fr;
-> "display: grid" active le mode grille. 
-> "grid-template-columns" définit le nombre et la taille des colonnes. "1fr" signifie "1 fraction de l'espace disponible". En l'écrivant 4 fois, on crée 4 colonnes strictement identiques qui occupent toute la largeur.

5. Le Responsive (Les Media Queries) :
@media screen and (max-width: 500px) { ... }
-> Cette règle est un point de rupture (breakpoint). Elle dit au navigateur : "Dès que la largeur de l'écran passe en dessous de 500 pixels (taille d'un téléphone), applique les règles CSS entre ces accolades". Ici, on passe de 4 colonnes ("1fr 1fr 1fr 1fr") à 2 colonnes ("1fr 1fr").

--------------------------------------------------------------------
PARTIE 3 : L'HABILLAGE CSS SPÉCIFIQUE (Le Theming du Restaurant)
--------------------------------------------------------------------

1. L'écrasement des variables (La Cascade) :
Dans "formulaire.css", on redéclare un bloc ":root" avec de nouvelles couleurs (ex: le rouge #8b1a1a). 
-> En CSS (Cascading Style Sheets), la dernière règle lue par le navigateur écrase la précédente. Comme "formulaire.css" est appelé en dernier dans le HTML, ses variables rouges remplacent les variables vertes du CSS générique, sans que l'on ait à modifier le code de base !

2. Le système d'affichage des erreurs :
.message-erreur { display: none; }
.groupe-champ.erreur .message-erreur { display: block; }
-> Par défaut, le message d'erreur texte est invisible (display: none).
-> La deuxième ligne est de la sélection conditionnelle : "Cherche un élément ayant la classe 'message-erreur', mais SEULEMENT S'IL EST À L'INTÉRIEUR d'un élément ayant à la fois les classes 'groupe-champ' ET 'erreur'". 
-> C'est le JavaScript qui ajoutera le mot "erreur" à la div parente en cas de problème, ce qui déclenchera instantanément l'apparition du texte et le changement de couleur des bordures.

--------------------------------------------------------------------
PARTIE 4 : L'INTERACTIVITÉ JAVASCRIPT (validation.js)
--------------------------------------------------------------------

1. Sécuriser le chargement du script :
document.addEventListener('DOMContentLoaded', () => { ... })
-> Le JS est souvent plus rapide que l'affichage visuel de la page. Si le JS cherche le formulaire avant qu'il ne soit dessiné à l'écran, il plantera. Cet "écouteur d'événement" force le JS à attendre le signal "La page est prête" avant de s'exécuter.

2. Bloquer l'envoi par défaut :
event.preventDefault();
-> Quand on clique sur le bouton "Submit" d'un formulaire, le comportement naturel du navigateur est de recharger la page pour envoyer les données à un serveur. Cette commande "prévient" (bloque) ce comportement par défaut. Le formulaire reste affiché, ce qui nous laisse le temps de faire nos calculs de vérification.

3. L'algorithme de la fonction réutilisable :
function validerChampAvecRegex(inputElement, regex) {
    const groupeParent = inputElement.parentElement;
    const valeur = inputElement.value.trim();
    // ... test de la regex ...
}
-> "inputElement.parentElement" : On utilise le "DOM Traversal" (navigation dans l'arbre HTML). Plutôt que de donner un ID spécifique (ex: "groupe-nom") à chaque appel, la fonction regarde l'input qu'on lui donne, et "remonte" d'un étage pour trouver la div qui l'englobe.
-> ".trim()" : C'est une fonction native de nettoyage. Si un utilisateur tape "  Jean  " avec des espaces au début et à la fin, le trim() transforme cela en "Jean" avant de le vérifier.

4. Explication des Expressions Régulières (Regex) :
Le Javascript utilise la méthode "regex.test(valeur)" qui renvoie "true" (vrai) ou "false" (faux).
-> /^[a-zA-ZÀ-ÿ\s-]{2,}$/ : Le "^" signifie "Le texte DOIT commencer par", et le "$" signifie "Le texte DOIT se terminer par". Les crochets [...] listent ce qui est autorisé (lettres minuscules, majuscules, accents, espaces \s et tirets). Le "{2,}" indique la quantité : "au moins 2 caractères, sans limite maximum". Si l'utilisateur tape le chiffre "1", la regex renvoie "false" car les chiffres ne sont pas dans les crochets.

5. Le Bilan et la validation finale :
let formulaireEstValide = true;
-> On initialise une variable booléenne (Vrai/Faux) qu'on appelle un "drapeau" (flag). On part du principe que tout est bon (true).
-> Ensuite, on effectue tous nos tests (if... false). Si un seul test échoue, notre drapeau tombe à "false".
-> À la toute fin du code, on fait le bilan : "if (formulaireEstValide === true)". Si c'est le cas, cela prouve qu'absolument aucun test n'a échoué. On déclenche alors la fonction "alert()" pour afficher la fenêtre pop-up de succès, et la fonction native "form.reset()" qui efface tout le texte tapé par l'utilisateur pour remettre le formulaire à neuf.
====================================================================