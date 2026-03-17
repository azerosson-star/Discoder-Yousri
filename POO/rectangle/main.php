<?php

require "rectangle.php";
$rect = new rectangle(10,5);
echo "Longueur : ".$rect->getLongueur()."\n";
echo "Largeur : ".$rect->getLargeur()."\n";
echo "Périmètre : ".$rect->perimetre()."\n";
echo " Aire : ".$rect->aire()."\n";
echo " EstCarre : ".$rect->Estcarre();