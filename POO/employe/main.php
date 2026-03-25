<?php
require_once "employe.php";
require_once "agence.php";

// 1. Création des agences
$agenceNord = new Agence("Agence Nord", "10 rue de la Paix", "75000", "Paris");
$agenceSud = new Agence("Agence Sud", "5 avenue du Rhône", "69000", "Lyon");

// 2. Création des 5 employés rattachés à leurs agences (votre code d'origine mis à jour)
$empl1 = new Employe("tom", "tom", 1996, "tata", 1000, "rat", $agenceNord);
$empl2 = new Employe("popo", "papa", 2020, "policier", 3000, "chat", $agenceSud);
$empl3 = new Employe("pipo", "zizoi", 2015, "astronaute", 3100, "chien", $agenceNord);
$empl4 = new Employe("soso", "saza", 2010, "pompier", 4586, "bibou", $agenceSud);
$empl5 = new Employe("coco", "kiki", 2002, "babouche", 7589, "zazou", $agenceNord);

// 3. Création de la liste (Array)
$employes = [$empl1, $empl2, $empl3, $empl4, $empl5];

echo "========================================\n";
echo "           REPORTING ENTREPRISE         \n";
echo "========================================\n\n";


echo "1. Nombre total d'employés de l'entreprise : " . count($employes) . "\n\n";


usort($employes, function($a, $b) {
    $cmpNom = strcasecmp($a->getNom(), $b->getNom());
    if ($cmpNom === 0) {
        return strcasecmp($a->getPrenom(), $b->getPrenom());
    }
    return $cmpNom;
});

echo "2. Liste des employés (Ordre alphabétique : Nom puis Prénom) :\n";
foreach ($employes as $emp) {
    echo "   - " . $emp->getInfos() . "\n";
}
echo "\n";


usort($employes, function($a, $b) {
    $cmpService = strcasecmp($a->getService(), $b->getService());
    if ($cmpService === 0) {
        $cmpNom = strcasecmp($a->getNom(), $b->getNom());
        if ($cmpNom === 0) {
            return strcasecmp($a->getPrenom(), $b->getPrenom());
        }
        return $cmpNom;
    }
    return $cmpService;
});

echo "3. Liste des employés (Ordre : Service > Nom > Prénom) :\n";
foreach ($employes as $emp) {
    echo "   - " . $emp->getInfos() . "\n";
}
echo "\n";


$masseSalarialeTotale = 0;

foreach ($employes as $emp) {
    
    $coutEmploye = $emp->getSalaire() + $emp->prime();
    $masseSalarialeTotale += $coutEmploye;
}

echo "4. Masse salariale totale de l'entreprise : " . number_format($masseSalarialeTotale, 2, ',', ' ') . " €\n";

