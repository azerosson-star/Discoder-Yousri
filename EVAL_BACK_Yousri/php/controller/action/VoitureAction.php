<?php

var_dump($_POST);
$util = new Voiture($_POST);
switch ($_GET['mode']) {
    case 'Ajouter':
        VoitureService::insert($util);
        break;
    case 'Modifier':
        VoitureService::update($util);
        break;
    case 'Supprimer':
        VoitureService::delete($util->getIdVoiture());
        break;
    
    default:
        # code...
        break;
}