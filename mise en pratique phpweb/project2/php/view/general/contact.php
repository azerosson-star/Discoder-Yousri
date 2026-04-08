<?php

$contact=<<<HTML
        <h1 class="mb-1">Contact</h1>
        <form class="bg-white p-2 br-1 shadow flex flex-col">
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="nom@domaine.com">
            </div>
            <div class="form-group">
                <label class="form-label">Message</label>
                <input type="text" class="form-input" style="height: 100px;">
            </div>
            <button type="submit" class="btn bg-primary br-1">Envoyer</button>
        </form>
HTML;

echo $contact;