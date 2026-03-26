<?php

class Score 
{
    private $score;

    public function hydrate(array $donnees): void 
    {
        foreach ($donnees as $cle => $valeur) {
           
            $formatage = str_replace(' ', '', ucwords(str_replace('_', ' ', $cle)));
            $methode = 'set' . $formatage;

            if (method_exists($this, $methode)) {
                $this->$methode($valeur);
            }
        }
    }

    public function setScore($score): void 
    {
        $this->score = $score;
    }

    public function getScore() 
    {
        return $this->score;
    }




public function augmenteScore(){}







    }