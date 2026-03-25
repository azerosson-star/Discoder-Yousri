<?php

class Mot
{
    private $_code;

    private $_listepos;


    
    
   public function hydrate(array $donnees) {
        foreach ($donnees as $cle => $valeur) {
            
            
            $formatage = str_replace(' ', '', ucwords(str_replace('_', ' ', $cle)));
            
           
            $methode = 'set' . $formatage; 
            
            
            if (method_exists($this, $methode)) {
                $this->$methode($valeur);
            }
        }
        
        }


    public function setId($id) { 
        $this->id = (int) $id; 
    }
        public function setCode($code) { 
        $this->_code = ucfirst(strtolower($code));
    }
    public function setListePos($listepos) { 
        $this->_listepos = ucfirst(strtolower($listepos));
    }


     public function getCode() { return $this->_code; }
    public function getListePos() { return $this->_listepos; }







}    
 
    
    
    
    
    
    
    
    
    
























    
