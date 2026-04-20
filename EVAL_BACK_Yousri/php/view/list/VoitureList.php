<?php

echo '<h1>Liste des voitures issus de la base de données</h1>';
echo '<div class=grid>';
echo '<a href="" class="spanGrid"><my-icon name="plus-' . Parametre::getTypeIcon() . '" ></my-icon></a>';
$listeVoiture = VoitureService::select(null);
foreach ($listeVoiture as $uti) {
   echo '<div>'.$uti->getLogin().'</div>';
   echo'<div></div>';
    echo '<a href="?page=VoitureForm&mode=Modifier&id='.$uti->getIdVoiture().'"><my-icon name=edit-'.Parametre::getTypeIcon().'></my-icon></a>';
   echo '<a href="?page=VoitureForm&mode=Supprimer&id='.$uti->getIdVoiture().'"><my-icon name=trash-'.Parametre::getTypeIcon().'></my-icon></a>';}

echo '</div>';
