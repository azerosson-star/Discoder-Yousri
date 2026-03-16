<?php
$nombres = [10, 20, 30, 40, 50];
echo "Original : [" . implode(", ", $nombres) . "]";

// array_reverse crée un nouveau tableau inversé (contrairement à .reverse() en Python)
$nombres_inverses = array_reverse($nombres);

echo "Inversé  : [" . implode(", ", $nombres_inverses) . "]";
