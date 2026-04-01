<?php
$navInfo = [];

$navInfo[] = new Nav(["libelle"=>"Accueil","icone"=>"house","reference"=>"index.php?page=accueil","couleur"=>"bleu"]);
$navInfo[] = new Nav(["libelle"=>"Produits","icone"=>"box","reference"=>"index.php?page=produits","couleur"=>"rouge"]);
$navInfo[] = new Nav(["libelle"=>"Contact","icone"=>"envelope","reference"=>"index.php?page=contact","couleur"=>"vert"]);

echo '   <header class="bg-dark p-1">
        <nav class="flex justify-between align-center container">
            <h2>Site 1</h2>
            <div class="flex gap-1">';

foreach ($navInfo as $value) {
    echo '<a href="'.$value->getReference().'" class="td-none nav-icon" >
    <span class="fas fa-'.$value->getIcone().'"></span>
    <span class="nav-text '.$value->getCouleur().'">'.$value->getLibelle().'</span></a>';
}

echo '            </div>
        </nav>
    </header>
    <main class="container">
';
?>