<?php

function testerGagner($nbErreur,$tab)
{
if ($nbErreur >= NB_Erreur){
    return -1;
    }


if (in_array("_",$tab)){
    return 0;
    }
    return 1;
}
