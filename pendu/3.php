<?php

function testerLettre($lettre, $tab, $depart) {
    
    $positionsTrouvees = [];
    
   
    for ($i = $depart; $i < count($tab); $i++) {
        
        if ($tab[$i] === $lettre) {
         
            $positionsTrouvees[] = $i;
        }
    }
    
 
    return $positionsTrouvees;
}


echo "Cette méthode doit donner \n 1 \n 4 et ca donne \n" ; 
$t = array( 'B', 'O', 'N', 'J', 'O', 'U', 'R' ); 
$positions = testerLettre('O', $t, 0); 

foreach ($positions as $pos) 
{ 
    echo("position : ".$pos."\n"); 
} 

