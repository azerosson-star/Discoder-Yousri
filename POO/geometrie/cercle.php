<?php



class Cercle
{private $_diametre;
    public function __construct($diametre)
    { $this->setDiametre($diametre != null ? $diametre: "");}
    
    public function getDiametre()
    {
        return $this->_diametre;
    
    
    }
    public function setDiametre($diametre)
    {
        $this->_diametre = $diametre;}
        
        
        
        
    public function rayon(){
    
    $rayon = $this->getDiametre()/2;
    return $rayon;
    }


    public function aire(){
    $aire = sqrt($this->rayon()) * pi();
    return $aire;
    }
    
public function perimetre(){
$perimetre = (2*pi())*$this->rayon();
return $perimetre;
}

    public function AfficherCercle(){

$diametre = $this->getDiametre();
$rayon = $this->rayon();
$perimetre= $this->perimetre();
$aire= $this->Aire();

$aff= "Diamètre : $diametre Rayon : $rayon Perimetre: $perimetre  aire  : $aire " ;
return $aff;   
        
        }}

    