<?php

class DAO
{
    public static function select(?array $colonnes, string $table, ?array $conditions = null, ?string $orderBy = null, bool $api = false, bool $debug = false)
    {
        $str = json_encode($colonnes) . $table . json_encode($conditions) . $orderBy;
        if (!str_contains($str, ";")) { // si pas de ; on continue
            $bdd = DbConnect::getDb();
            if ($colonnes == null)
                $listeColonnes = "*";
            else
                $listeColonnes = implode(',', $colonnes);
            $reqString = "select " . $listeColonnes . " from " . ucFirst($table);
            $wher = conditionsSelect($conditions);
            $reqString .= $wher;
            $reqString .= $orderBy == null ? "" : " order by " . $orderBy;
            $requete = $bdd->prepare($reqString);
            if ($debug) var_dump($requete);
            $requete->execute();
            $liste = [];
            while ($donnees = $requete->fetch(PDO::FETCH_ASSOC)) {
                if ($api)
                    $liste[] = $donnees;
                else
                    $liste[] = new $table($donnees);
            }
            return $liste;
        }
    }

    public static function findById($id,$table)
    {
        return DAO::select(null,$table,["id".ucFirst($table)=>$id]);
    }
}
