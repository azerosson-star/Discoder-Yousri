<?php

function hashage($texte)
{
    $hashe = md5(md5($texte) . "1");
    return $hashe;
}

/**
 * Appel le getter en fonction du nom de l'attribut (chaine) dans la classe de $obj
 *
 * @param [type] $obj
 * @param [type] $chaine
 * @return void
 */
function appelGet($obj, $chaine)
{
    $methode = 'get' . ucfirst($chaine);
    return call_user_func(array($obj, $methode));
}


/**
 * Crée un select a partir des informations passées en parametre
 *
 * @param integer $valeur => Id de l'element a Selectionner
 * 
 * @param string $table => contient Nom de la table sur laquelle la requête sera effectuée.
 * Exemple : nomTable => "FROM nomTable"
 * 
 * @param array $nomColonnes => contient le noms des champs désirés dans la requête.
 * Exemple :  [nomColonne1,nomColonne2] => "SELECT nomColonne1, nomColonne2"
 * 
 * @param string $attributs => attributs attendu dans la balise select
 * 
 * Exemples : <select class="filtrefiche" data-serie=3 >
 * 
 * @param array|null $condition => null par défaut, attendu un tableau associatif 
 * qui peut prendre plusieurs formes en fonction de la complexité des conditions.
 *
 *  Exemples : tableau associatif
 *  [nomColonne => '1'] => "WHERE nomColonne = 1"
 *  [nomColonne => ['1','3']] => "WHERE nomColonne in (1,3)"
 *  [nomColonne => '%abcd%'] => "WHERE nomColonne like "%abcd%"
 *  [nomColonne => '1->5'] => "WHERE nomColonne BETWEEN 1 and 5 "
 *  Si il y a plusieurs conditions alors :
 *  [nomColonne1 => '1', nomColonne2 => '%abcd%' ] => "WHERE nomColonne1 = 1 AND nomColonne2 LIKE "%abcd%"
 * 
 * @param string|null $orderBy $orderBy => null par défaut, contient un string qui contient les noms de colonnes et le type de tri
 * Exemple :"nomColonne1 , nomColonne2 DESC" => "Order By nomColonne1 , nomColonne2 DESC"
 * 
 * @param string|null $attributId $attributId => null par défaut, contient un string qui contient le name à donner au formulaire s'il est différent de la table
 * 
 * @param string $invite l'invite de la combobox
 * @return void
 */
function creerSelect(?int $valeur, string $table, array $nomColonnes, ?string $attributs = "", ?array $condition = null, ?string $orderBy = null, ?string $attributId = null, string $invite = "choisissez")
{
    $nomId = $table::getAttributes()[0];
    $atrId = ($attributId == null ? $nomId : $attributId); // par defaut l'Id de la table

    $select = '<select id="' . $atrId . '" name="' . $atrId . '"' . $attributs . '>';
    $servic = $table . 'Service';
    $libelle = $nomColonnes;
    array_push($nomColonnes, $nomId); // ajoute l'id à la liste des colonnes necessaires
    $liste = $servic::select($nomColonnes, $condition, $orderBy, false, false);
    if ($valeur == null) {
        $select .= '<option value="" SELECTED>' . $invite . '</option>';
    } else {
        $select .= '<option value="">' . $invite . '</option>';
    }
    foreach ($liste as $elt) {
        $content = "";
        foreach ($libelle as $value) {
            $content .= appelGet($elt, $value) . " | ";
        }

        $content = substr($content, 0, -3);

        if ($valeur == appelGet($elt, $nomId)) {
            $select .= '<option value="' . appelGet($elt, $nomId) . '" SELECTED>' . $content . '</option>';
        } else {
            $select .= '<option value="' . appelGet($elt, $nomId) . '">' . $content . '</option>';
        }
    }
    $select .= "</select>";
    return $select;
}
/* @param array $conditions => null par défaut, attendu un tableau associatif 
	 * qui peut prendre plusieurs formes en fonction de la complexité des conditions.
	 *  Exemples : tableau associatif
	 *  [nomColonne => '1'] => "WHERE nomColonne = 1"
	 *  [nomColonne => ''] => "WHERE nomColonne is null "
	 *  [nomColonne => ['1','3']] => "WHERE nomColonne in (1,3)"
	 *  [nomColonne => '%abcd%'] => "WHERE nomColonne like "%abcd%" "
	 *  [nomColonne => '1->5'] => "WHERE nomColonne BETWEEN 1 and 5 "
	 *  Si il y a plusieurs conditions alors :
	 *  [nomColonne1 => '1', nomColonne2 => '%abcd%' ] => "WHERE nomColonne1 = 1 AND nomColonne2 LIKE "%abcd%"
	 * 	[fullTexte]=>'test'=> "WHERE nomColonne1 like "%test%" OR nomColonne2 LIKE "%test%"
	 */
function conditionsSelect(?array $conditions = null)
{
    if ($conditions == null) // tableau condition vide => pas de where
        return "";
    $reponse = " WHERE ";
    foreach ($conditions as $key => $value) {
        if ($key != "fullTexte") {

            if (is_array($value)) { // si la valeur est un tableau =>  [nomColonne => ['1','3']] => "WHERE nomColonne in (1,3)"
                $reponse .= $key . " in (";
                foreach ($value as $item) { // on parcours les items pour faire le IN
                    $reponse .= $item . ",";
                }
                $reponse  = substr($reponse, 0, -1); // on enleve la dernière virgule
                $reponse .= ") AND ";
            } else {            // la valeur est une chaine
                if ($value == "") { // une chaine vide => [nomColonne => ''] => "WHERE nomColonne is null "
                    $reponse .= $key . " is null AND ";
                } else if (strpos($value, "%") !== false) { // contient un % =>[nomColonne => '%abcd%'] => "WHERE nomColonne like "%abcd%" "
                    $reponse .= $key . " like '" . $value . "' AND ";
                } else if (strpos($value, "->") !== false) { // contient un -> =>[nomColonne => '1->5'] => "WHERE nomColonne BETWEEN 1 and 5 "
                    $tab      = explode("->", $value);           // on recupere les valeurs avant et apres le symbole
                    $reponse .= $key . " between " . $tab[0] . " AND " . $tab[1] . " AND ";
                } else { // cas classique =>[nomColonne => '1'] => "WHERE nomColonne = 1"
                    $reponse .= $key . " = '" . $value . "' AND ";
                }
            }
            $reponse = substr($reponse, 0, -4);
        } else {
            $listeColonne = Voiture::getAttributes();
            foreach ($listeColonne as $colo) {

                $reponse .= $colo . " like '%" . $value . "%' OR "; // [fullTexte]=>'test'=> "WHERE nomColonne1 like "%test%" OR nomColonne2 LIKE "%test%"
            }
            $reponse  = substr($reponse, 0, -3); // on enleve le dernier OR
        }
    }

    return $reponse;
}
