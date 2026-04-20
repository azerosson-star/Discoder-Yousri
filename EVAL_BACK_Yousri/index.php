<?php

function ChargerClasse($classe)
{
    if (file_exists("./php/controller/classes/" . $classe . ".Class.php"))
        require "./php/controller/classes/" . $classe . ".Class.php";
    else
        require "./php/model/services/" . $classe . ".Class.php";
}
spl_autoload_register("ChargerClasse");
require "php/controller/routeur.php";
require "php/controller/helpers.php";
session_start();

if(isset($_SESSION['voiture'])) var_dump($_SESSION);
Parametre::init();
DbConnect::init();
chargerPage();
