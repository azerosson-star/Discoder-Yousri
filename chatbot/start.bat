@echo off
echo ========================================
echo Demarrage du Chatbot FastAPI
echo ========================================
echo.

REM Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    pause
    exit /b 1
)

echo [1/3] Verification des dependances...
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo Installation des dependances...
    pip install -r requirements.txt
) else (
    echo Dependances OK
)

echo.
echo [2/3] Verification de la base de donnees...
if exist chatbot.db (
    echo Base de donnees trouvee: chatbot.db
) else (
    echo Creation de la base de donnees...
)

echo.
echo [3/3] Demarrage du serveur...
echo.
echo ========================================
echo  Serveur accessible sur:
echo  http://localhost:8000
echo ========================================
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python main.py
