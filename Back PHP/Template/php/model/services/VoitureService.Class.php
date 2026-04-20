<?php


class VoitureService
{
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
    public static function select(?array $colonnes, ?array $conditions = null, ?string $orderBy = null, bool $api = false, bool $debug=false)
    {
        return DAO::select($colonnes,"Voiture",$conditions,$orderBy,$api,$debug);
    }

    public static function findByLogin($marque)
    {
        $bdd = DbConnect::getDb();
        $reqString = "select * from voiture where marque = :marque";
        $requete = $bdd->prepare($reqString);
        $requete->bindValue(":marque",$marque);
        $requete->execute();
        while ($donnees = $requete->fetch(PDO::FETCH_ASSOC)) {
            $voiture = new Voiture($donnees);
        }
        return $voiture;
    }
    public static function findById($id)
    {
        $bdd = DbConnect::getDb();
        $reqString = "select * from voiture where idVoiture = :id";
        $requete = $bdd->prepare($reqString);
        $requete->bindValue(":id", $id);
        $requete->execute();
        while ($donnees = $requete->fetch(PDO::FETCH_ASSOC)) {
            $voiture = new Voiture($donnees);
        }
        return $voiture;
    }

    static function insert($prod)
    {
        $db = DbConnect::getDb();
        $req = "insert into voiture (marque, modele,nbkilometres) VALUES (:marque,:modele,:nbkilometres)";
        $requete = $db->prepare($req);
        $requete->bindValue(':marque', $prod->getMarque(), PDO::PARAM_STR);
        $requete->bindValue(':modele', $prod->getModele(), PDO::PARAM_STR);
        $requete->bindValue(':nbkilometres', $prod->getNbKilometres(), PDO::PARAM_STR);
        $requete->execute();
        $requete->closeCursor();
    }

    static function update($prod)
    {
        $db = DbConnect::getDb();
        $req = "UPDATE voiture SET marque=:marque,modele=:modele, nbkilometres=:nbkilometres WHERE idVoiture=:idVoiture";
        $requete = $db->prepare($req);
        $requete->bindValue(':marque', $prod->getMarque(), PDO::PARAM_STR);
        $requete->bindValue(':modele', $prod->getModele(), PDO::PARAM_STR);
        $requete->bindValue(':nbkilometres', $prod->getNbKilometres(), PDO::PARAM_STR);
        $requete->bindValue(':idVoiture', $prod->getIdVoiture(), PDO::PARAM_STR);
        $requete->execute();
        $requete->closeCursor();
    }

    static function delete($id)
    {
        $db = DbConnect::getDb();
        $req = "DELETE FROM voiture WHERE idVoiture=:idVoiture";
        $requete = $db->prepare($req);
        $requete->bindValue(':idVoiture', $id);
        $requete->execute();
        $requete->closeCursor();
    }
}
