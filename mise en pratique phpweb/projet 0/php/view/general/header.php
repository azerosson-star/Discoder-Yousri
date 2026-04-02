<?php


$navInfo[] = new Nav(["libelle"=>"Accueil","icone"=>"house","reference"=>"index.php?page=accueil","couleur"=>"bleu"]);
$navInfo[] = new Nav(["libelle"=>"Produits","icone"=>"product","reference"=>"?page=produits","couleur"=>"rouge"]);
$navInfo[] = new Nav(["libelle"=>"Contact","icone"=>"contact","reference"=>"?page=contact","couleur"=>"vert"]);


$nomProjet = Parametres::getNomProjet();

// 2. Build the navigation links HTML using a loop BEFORE the Heredoc
$navLinksHtml = '';
foreach ($navInfo as $value) {
    // Using standard string concatenation to build the HTML for the links
    $navLinksHtml .= '<a href="' . $value->getReference() . '" class="td-none nav-icon">';
    $navLinksHtml .= '<span class="fas fa-' . $value->getIcone() . '"></span>';
    $navLinksHtml .= '<span class="nav-text ' . $value->getCouleur() . '">' . $value->getLibelle() . '</span></a>';
}
$header=<<<HTML
 <header class="bg-dark p-1">
        <nav class="flex justify-between align-center container">
            <h2>{$nomProjet}</h2>
            <div class="flex gap-1">';
                {$navLinksHtml}
            </div>
        </nav>
    </header>
    <main class="container">

HTML;