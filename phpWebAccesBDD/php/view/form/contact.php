<?php
echo '
        <h1 class="mb-1">Contactez-nous</h1>
        <form class="bg-white p-2 br-1 shadow flex flex-col">
            <div class="form-group">
                <label class="form-label">Nom complet</label>
                <input type="text" class="form-input" placeholder="Votre nom">
            </div>
            <div class="form-group">
                <label class="form-label">Email</label>
                <input type="email" class="form-input" placeholder="nom@domaine.com">
            </div>
            <div class="form-group">
                <label class="form-label">Mot de passe</label>
                <input type="password" class="form-input">
            </div>
            <div class="form-group">
                <label class="form-label">Sujet</label>
                <select class="form-input">
                    <option>Question technique</option>
                    <option>Service client</option>
                </select>
            </div>
            <div class="form-row mb-1">
                <label class="form-label mr-1">Priorité :</label>
                <input type="radio" name="prio" id="p1" checked> <label for="p1">Basse</label>
                <input type="radio" name="prio" id="p2"> <label for="p2">Haute</label>
            </div>
            <div class="form-row mb-1">
                <input type="checkbox" id="rgpd"> <label for="rgpd">J\'accepte la politique de confidentialité</label>
            </div>
            <button type="submit" class="btn bg-primary br-1">Envoyer le message</button>
        </form>
    ';