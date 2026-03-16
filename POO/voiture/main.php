<?php
 require "Voiture.Class.php";

    $voiture1 = new Voiture();
    $voiture1->_couleur = readline("Entrez la couleur de votre voiture : ");
    $voiture1->_marque = readline("Entrez la marque de votre voiture : ");
    $voiture1->_modele = readline("Entrez le modèle de votre voiture : ");
    $voiture1->_km = (int)readline("Entrez les kilomètres de votre voiture : ");
    $voiture1->_motor = readline("Entrez le type de moteur de votre voiture : ");
 