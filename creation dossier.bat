@echo off
chcp 65001 >nul :: gestion des accents

:: Demande du nom du projet
set /p NomProjet=Entrez le nom du dossier du projet (ex: MonSiteWeb) :

if "%NomProjet%"=="" (
    set NomProjet=MonProjet
    echo Nom vide ^> utilisation du nom par défaut : %NomProjet%
)

:: Chemin courant
set CheminRacine=%cd%\%NomProjet%

:: Sécurité : si le dossier existe déjà
if exist "%CheminRacine%" (
    echo.
    echo ⚠️ Le dossier "%NomProjet%" existe deja !
    echo Annulation pour eviter d'ecraser les fichiers.
    pause
    exit /b
)

:: Création du dossier principal
mkdir "%CheminRacine%"

echo.
echo 📍 Arborescence creee dans :
echo %CheminRacine%
echo ==========================================
echo.

:: Liste des dossiers
set dossiers=css js images assets docs php php\controller php\controller\action php\controller\classes php\model php\model\api php\model\services php\view php\view\form php\view\general php\view\list sql

for %%d in (%dossiers%) do (
    mkdir "%CheminRacine%\%%d"
    echo 📁 Cree : %%d

    :: Création index.php
    if not exist "%CheminRacine%\%%d\index.php" (
        (
        echo ^<?php
        echo // Protection contre l'affichage du contenu du dossier
        echo http_response_code(403);
        echo echo 'Acces interdit.';
        echo exit;
        ) > "%CheminRacine%\%%d\index.php"

        echo    └─ 📄 index.php (sécurité)
    )
)

:: Fichiers racine
if not exist "%CheminRacine%\index.php" (
    (
    echo ^<?php
    echo // Page d'accueil principale de ton projet
    echo echo '^<h1^>Bienvenue sur %NomProjet% !^</h1^>';
    ) > "%CheminRacine%\index.php"

    echo 📄 Fichier racine cree : index.php
)

if not exist "%CheminRacine%\config.json" (
    type nul > "%CheminRacine%\config.json"
    echo 📄 Fichier racine cree : config.json
)

echo.
echo 🎉 Tout est termine avec succes !
echo Le projet "%NomProjet%" a ete cree.
echo.
pause