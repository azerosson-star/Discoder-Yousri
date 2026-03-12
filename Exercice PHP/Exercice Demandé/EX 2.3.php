<?php
$HT=readline("entrer le prix HT : ");
$NBart=readline("entrer le nombre d'articles : ");
$prixHTtotal = ($HT)*($NBart);
$Taxe=readline("entrer le taux de taxe : ");
$prixTTC= ($prixHTtotal)+($prixHTtotal)*(($Taxe)/100);
echo "le prix total TTC est de $prixTTC";
