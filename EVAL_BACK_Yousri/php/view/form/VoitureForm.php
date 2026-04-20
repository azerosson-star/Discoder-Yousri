<?php


$id =  isset($_GET['id'])?$_GET['id']:"";  
$disabled="";
switch ($_GET['mode'])
{
    case "Ajouter" :
        $uti=new Voiture();
        $disabled="";
        break;
    case "Modifier" : 
        $uti = VoitureService::findById($id);
        $disabled="";
        break;
    case "Supprimer":
        $uti = VoitureService::findById($id);
        $disabled = " disabled ";
        break;
}
echo '
<form action="?page=VoitureAction&mode='.$_GET['mode'].'" method="post">
    <input hidden type="text" id=idVoiture name=idVoiture>
    <label for=Marque">Marque</label>
    <input type="text" id=Marque name=Marque  '.$disabled.' value = '.$uti->getMarque().'>
    <br/>
    <label for="Modele">Modele</label>
    <input type="text" id=Modele name=Modele  '.$disabled.' value = '.$uti->getModele().'>
    <br/>';
    
    ;
    // $listeRoles = RoleService::select();
    // echo ' <select id=idRole name=idRole  '.$disabled.'>';
    // foreach ($listeRoles as $role) {
        
    //     echo '<option value='.$role->getIdRole() . ($role->getIdRole()==$uti->getIdRole()?" selected ":" ").'>'.$role->getLibelle().'</option>';
    // }
    // echo '</select>';
   
    echo '
    <br/>
    <button type=submit >Valider</button>
</form>';

//<input type="text" id=idRole name=idRole   '.$disabled.' value = '.$uti->getIdRole().'>