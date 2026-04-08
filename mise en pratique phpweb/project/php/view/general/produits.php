<?php

$produit=<<<HTML
        <h1 class="mb-1">Nos Articles (Vue Cartes)</h1>
        <div class="prod-grid">
            <div class="prod-card bg-white br-1 shadow">
                <div class="prod-img-ph"></div>
                <div class="p-1 flex flex-col gap-1">
                    <h3>Écran 27"</h3>
                    <div class="flex justify-between"><span>Réf: ECR-01</span> <span>EAN: 112233</span></div>
                    <div class="flex justify-between"><span>Stock: 8</span> <strong>199,99 €</strong></div>
                </div>
            </div>
            <div class="prod-card bg-white br-1 shadow">
                <div class="prod-img-ph"></div>
                <div class="p-1 flex flex-col gap-1">
                    <h3>Casque Audio</h3>
                    <div class="flex justify-between"><span>Réf: CSQ-02</span> <span>EAN: 445566</span></div>
                    <div class="flex justify-between"><span>Stock: 21</span> <strong>89,00 €</strong></div>
                </div>
            </div>
        </div>
HTML;

echo $produit;