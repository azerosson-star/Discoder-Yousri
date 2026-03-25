<?php

function coderMot($mot) {
    
    $longueur = strlen($mot);
    
   
    $tableauCode = [];
    
   
    for ($i = 0; $i < $longueur; $i++) {
        $tableauCode[] = '_';
    }
    
    return $tableauCode;
}


$test = "bonjour";

print_r(coderMot($test));

