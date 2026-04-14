<?php

$inscription = <<<HTML
<h1 class="mb-1">Inscription</h1>
<form class="bg-white p-2 br-1 shadow flex flex-col gap-1" method="POST" action="">
    <div class="form-group">
        <label class="form-label">nom</label>
        <input type="text" class="form-input" placeholder="Votre nom d'utilisateur"required name="username" id="username">
    </div>
    <div class="form-group">
        <label class="form-label">email</label>
        <input type="email" class="form-input" placeholder="Votre email" required name="email" id="email" >
    </div>
    <div class="form-group">
        <label class="form-label">mot de passe</label>
        <input type="password" class="form-input" placeholder="Votre mot de passe" required name="password" id="password">
    </div>
    <input type="submit" class="btn btn-primary" value="S'inscrire">
</form>
HTML;

echo $inscription;







