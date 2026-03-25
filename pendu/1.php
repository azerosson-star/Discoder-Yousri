<?php

$t = array( 'B', 'O', 'N', 'J', 'O', 'U', 'R' );
            Echo "Cette méthode doit donner B O N J O U R et ca donne : " . afficherTableau($t);
function afficherTableau($t){
    $result = "";
    foreach($t as $element){
        $result .= $element . " ";
    }
    return $result;
}