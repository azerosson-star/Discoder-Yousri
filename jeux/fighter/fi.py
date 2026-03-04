import pygame
import sys
import random

# ================================================
# NEON FIST v10.0 - ULTIMATE ARCADE EDITION 🔥
# ================================================

pygame.init()
L, H = 800, 450
ecran = pygame.display.set_mode((L, H))
pygame.display.set_caption("NEON FIST - ULTIMATE ARCADE")
horloge = pygame.time.Clock()

# --- Paramètres de Jeu ---
LIMIT_Y_HAUT = 260
LIMIT_Y_BAS = 380
GRAVITE = 0.7

# ====================== CHARGEMENT ASSETS ======================
def get_anim(path, frames, w=64, h=96):
    """Charge et découpe une spritesheet."""
    sheet = pygame.image.load(path).convert_alpha()
    return [sheet.subsurface(pygame.Rect(i*w, 0, w, h)) for i in range(frames)]

class Assets:
    def __init__(self):
        # Décors & UI
        self.back = pygame.image.load("fighter/assets/Stage Layers/back.png").convert()
        self.fore = pygame.image.load("fighter/assets/Stage Layers/fore.png").convert_alpha()
        self.shadow = pygame.image.load("fighter/assets/Sprites/shadow.png").convert_alpha()
        
        # Brawler Girl - Panel complet
        self.hero = {
            "idle": get_anim("fighter/assets/Spritesheets/Brawler Girl/idle.png", 4),
            "walk": get_anim("fighter/assets/Spritesheets/Brawler Girl/walk.png", 10),
            "punch": get_anim("fighter/assets/Spritesheets/Brawler Girl/punch.png", 3),
            "jump": get_anim("fighter/assets/Spritesheets/Brawler Girl/jump.png", 4),
            "dive": get_anim("fighter/assets/Spritesheets/Brawler Girl/dive_kick.png", 5),
            "hurt": get_anim("fighter/assets/Spritesheets/Brawler Girl/hurt.png", 2)
        }
        
        # Collectibles
        self.coin = [
            pygame.image.load("fighter/assets/Stage Layers/props/Ethereum/ethereum-1.png").convert_alpha(),
            pygame.image.load("fighter/assets/Stage Layers/props/Ethereum/ethereum-2.png").convert_alpha()
        ]

asst = Assets()

# ====================== CLASSES ENTITÉS ======================
class Personnage:
    def __init__(self, x, y, anims):
        self.pos = pygame.Vector2(x, y) # Position au sol (pieds)
        self.h = 0 # Hauteur du saut
        self.vel_h = 0
        self.anims = anims
        self.etat = "idle"
        self.frame = 0
        self.dir = 1
        self.vivant = True

    def dessiner(self, surf, scroll):
        # 1. Ombre dynamique (Z-Sorting)
        scale = max(0.2, 1.0 - (self.h / 150))
        sh_w = int(48 * scale)
        sh_img = pygame.transform.scale(asst.shadow, (sh_w, int(15 * scale)))
        surf.blit(sh_img, (self.pos.x - sh_w//2 - scroll, self.pos.y - 5))
        
        # 2. Sprite
        img = self.anims[self.etat][int(self.frame) % len(self.anims[self.etat])]
        if self.dir == -1: img = pygame.transform.flip(img, True, False)
        # On dessine à (pos.x, pos.y - hauteur_saut - hauteur_sprite)
        surf.blit(img, (self.pos.x - 32 - scroll, self.pos.y - self.h - 90))

    def animer(self, v=0.15):
        self.frame += v
        if self.frame >= len(self.anims[self.etat]):
            if self.etat in ["punch", "dive", "hurt"]: self.etat = "idle"
            self.frame = 0

class Heroine(Personnage):
    def update(self, k):
        # Mouvements 8-directions
        move = pygame.Vector2(0, 0)
        if k[pygame.K_LEFT]: move.x = -5; self.dir = -1
        if k[pygame.K_RIGHT]: move.x = 5; self.dir = 1
        if k[pygame.K_UP]: move.y = -3
        if k[pygame.K_DOWN]: move.y = 3
        
        if move.length() > 0 and self.h == 0:
            self.pos += move
            self.etat = "walk"
            # Bridage à la route
            self.pos.y = max(LIMIT_Y_HAUT, min(LIMIT_Y_BAS, self.pos.y))
        elif self.h == 0:
            self.etat = "idle"

        # Saut et Dive Kick
        if k[pygame.K_SPACE] and self.h == 0:
            self.vel_h = 12
        
        if self.h > 0 or self.vel_h != 0:
            self.h += self.vel_h
            self.vel_h -= GRAVITE
            self.etat = "jump"
            if k[pygame.K_k]: # Dive Kick en l'air !
                self.etat = "dive"
                self.vel_h = -10 # Accélère la chute
            
            if self.h <= 0:
                self.h = 0; self.vel_h = 0; self.etat = "idle"

        self.animer()

# ====================== BOUCLE PRINCIPALE ======================
def main():
    joueur = Heroine(100, 320, asst.hero)
    scroll = 0
    coins = [{"pos": pygame.Vector2(500, 300), "f": 0}]

    while True:
        horloge.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()

        # Logique
        keys = pygame.key.get_pressed()
        joueur.update(keys)
        scroll += (joueur.pos.x - 300 - scroll) * 0.1

        # Rendu
        ecran.blit(asst.back, (-(scroll * 0.2) % L - L, 0))
        ecran.blit(asst.back, (-(scroll * 0.2) % L, 0))
        ecran.blit(asst.fore, (-(scroll * 0.8) % L - L, 0))
        ecran.blit(asst.fore, (-(scroll * 0.8) % L, 0))

        # Z-Sorting : On trie tout par coordonnée Y pour le rendu
        # Ici on dessine les pièces d'abord
        for c in coins:
            c["f"] += 0.1
            img = asst.coin[int(c["f"]) % 2]
            ecran.blit(img, (c["pos"].x - scroll, c["pos"].y - 20))

        joueur.dessiner(ecran, scroll)
        pygame.display.flip()

if __name__ == "__main__": main()