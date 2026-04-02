<?php
$nomprojet=Parametres::getNomProjet();
$acceuil=<<<HTML

<h1 class="acceuil">Bienvenue sur $nomprojet</h1>

HTML;

echo $acceuil;