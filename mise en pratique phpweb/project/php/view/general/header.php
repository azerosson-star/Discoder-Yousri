<?php



$header=<<<HTML
<body class="flex">
    <input type="checkbox" id="nav-toggle" class="menu-toggle">
    <label for="nav-toggle" class="burger-btn bg-dark" style="display:none;">☰</label>

    <nav class="sidebar bg-dark p-2 flex flex-col h-100vh w-sidebar gap-1 fixed">
        <h2>Site 2</h2>
        <a href="index.php?page=acceuil" class="td-none">Accueil</a>
        <a href="index.php?page=produits" class="td-none">Produits</a>
        <a href="index.php?page=contact" class="td-none">Contact</a>
        <a href="index.php?page=inscription" class="td-none">Inscription</a>
    </nav>
    <main class="flex-grow p-2 ml-sidebar pt-mobile">
HTML;
echo $header;