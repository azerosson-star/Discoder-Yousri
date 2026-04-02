<?php
// Protection contre l'affichage du contenu du dossier
http_response_code(403);
echo 'Acces interdit.';
exit;
