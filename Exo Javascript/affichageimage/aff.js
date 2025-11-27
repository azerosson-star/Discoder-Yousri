// 1. Créer et ajouter le titre (facultatif, tu peux aussi le laisser dans le HTML)
const h1 = document.createElement("h1");
h1.textContent = "Le titre de ma page";
h1.style.textAlign = "center";
h1.style.margin = "50px";
document.body.prepend(h1); // met le titre en haut

// 2. Récupérer le bouton qui existe déjà dans le HTML
const bouton = document.getElementById("btncouleur");

// 3. Fonction qui génère une couleur aléatoire et change le fond
bouton.addEventListener("click", () => {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
    
    // Bonus : petite animation douce
    document.body.style.transition = "background-color 0.6s ease";
});

// Style rapide du bouton pour qu’il soit joli
bouton.style.padding = "15px 30px";
bouton.style.fontSize = "18px";
bouton.style.cursor = "pointer";
bouton.style.borderRadius = "12px";
bouton.style.border = "none";
bouton.style.backgroundColor = "#2d3436";
bouton.style.color = "white";
bouton.style.display = "block";
bouton.style.margin = "30px auto";