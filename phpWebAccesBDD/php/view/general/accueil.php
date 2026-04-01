<?php


echo '

        <h1 class="mb-1 text-center">Bienvenue sur '.Parametres::getNomProjet().'</h1>
        <p class="text-center p-2 bg-white br-1 shadow">Ceci est une page d\'accueil avec du texte fixe. Notre navbar devient des icônes sur mobile.</p>
        
        <input type="checkbox" id="ai-toggle" class="toggle-checkbox">
        <label for="ai-toggle" class="ai-btn bg-primary fixed bottom-0 right-0 shadow">💬</label>
        <my-icon name="bell-duotone"></my-icon>
        <div class="ai-frame fixed bg-white shadow br-1 p-1 flex-col">
            <h3 class="mb-1">Assistant IA</h3>
            <div class="chat-bubble chat-left">Bonjour ! Je suis une IA générée en pur CSS.</div>
            <div class="chat-bubble chat-right">Impressionnant ! Comment ça marche ?</div>
            <div class="chat-bubble chat-left">Grâce au Checkbox Hack !</div>
        </div>
';
