<?php
$navInfo[] = new NavElement(["libelle"=>"Accueil","reference"=>"index.php?page=accueil","couleur"=>"bleu"]);
$navInfo[] = new NavElement(["libelle"=>"Voiture","reference"=>"?page=voiture","couleur"=>"rouge"]);
 echo '   <header class="bg-dark p-1">
        <nav class="flex justify-between align-center container">
            <h2>ECF</h2>
            <div class="flex gap-1">';
            $navInfo = Parametre::getNav();
foreach ($navInfo as $value) {
    echo '<a href='.$value->getReference().' class="td-none nav-icon" >
    <span class="fas fa-'.$value->getIcon().'"></span>
    <span class="nav-text ">'.$value->getNom().'</span></a>';
}
echo '            </div>
        </nav>
    </header>
    <main class="container">
';