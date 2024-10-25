import pygame
import pytmx
import os
import random
from entitee import Entitee
from creature import Creature
from joueur import Joueur
from pnj import Pnj  # Importer la classe PNJ

# Configuration initiale de la carte et de l'affichage
TAILLE_CARTE = 960  # Taille totale de la carte (960x960)
VITESSE_JOUEUR = 0.8  # Vitesse réduite de déplacement du joueur en pixels

# Fonction pour dessiner un bouton
def draw_button(surface, text, pos, width, height, color):
    pygame.draw.rect(surface, color, (pos[0], pos[1], width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(pos[0] + width // 2, pos[1] + height // 2))
    surface.blit(text_surface, text_rect)

# Fonction principale du jeu
def main():
    pygame.init()

    # Taille de l'écran
    screen = pygame.display.set_mode((TAILLE_CARTE, TAILLE_CARTE))

    # Charger la carte Tiled
    print("Chemin actuel :", os.getcwd())
    tmx_data = pytmx.load_pygame("src/level_data/map.tmx")

    # Charger la texture du joueur
    player_texture = pygame.image.load("sprites/fHero.png").convert_alpha()
    player_texture = pygame.transform.scale(player_texture, (16, 16))  # Redimensionne l'image à 16x16 pixels

    # Initialiser le joueur au centre de la carte
    joueur = Joueur([TAILLE_CARTE // 2, TAILLE_CARTE // 2], "Lucas", "Guerrier", {"argent": 100}, "Avatar")

    # Initialiser les créatures
    creatures = [
        Creature("Goblin", 100, 10, {}, {}) for _ in range(5)
    ]
    for creature in creatures:
        creature.x = random.randint(0, TAILLE_CARTE - 50)
        creature.y = random.randint(0, TAILLE_CARTE - 50)

    # Initialiser les PNJ avec leurs propres sprites
    pnjs = [
        Pnj((384, 406), "Forgeron", "Un marchand amical", {"vendeur": True, "argent": 50}, "Bonjour ! Que puis-je faire pour vous ?", "sprites/shrek.png"),
        Pnj((560, 406), "Armurier", "Un guide mystérieux", {"vendeur": True}, "Bienvenue dans notre monde !", "sprites/knight.png"),
        Pnj((384, 566), "Alchimiste", "Un vieux bougre", {"vendeur": True}, "Les secrets de cette terre sont puissants.", "sprites/necromancer.png")
    ]

    # Fonction pour dessiner la carte
    def draw_map(surface):
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    # Fonction pour dessiner les créatures
    def draw_creatures(surface):
        for creature in creatures:
            pygame.draw.circle(surface, (255, 0, 0), (creature.x, creature.y), 10)

    # Fonction pour dessiner le joueur
    def draw_joueur(surface, joueur):
        surface.blit(player_texture, joueur.pos)

    # Fonction pour dessiner les PNJ
    def draw_pnjs(surface):
        for pnj in pnjs:
            pnj.draw(surface)  # Utiliser la méthode de dessin

    # Boucle de jeu
    running = True
    current_pnj = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and current_pnj:
                mouse_pos = pygame.mouse.get_pos()
                button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
                button_rect = pygame.Rect(button_pos[0], button_pos[1], 140, 40)
                
                if button_rect.collidepoint(mouse_pos):
                    current_pnj.interaction(joueur)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:  # Haut
            joueur.pos[1] -= VITESSE_JOUEUR
        if keys[pygame.K_s]:  # Bas
            joueur.pos[1] += VITESSE_JOUEUR
        if keys[pygame.K_q]:  # Gauche
            joueur.pos[0] -= VITESSE_JOUEUR
        if keys[pygame.K_d]:  # Droite
            joueur.pos[0] += VITESSE_JOUEUR

        joueur.pos[0] = max(0, min(joueur.pos[0], TAILLE_CARTE - 16))
        joueur.pos[1] = max(0, min(joueur.pos[1], TAILLE_CARTE - 16))

        draw_map(screen)
        draw_creatures(screen)
        draw_joueur(screen, joueur)
        draw_pnjs(screen)

        joueur_pos = pygame.Vector2(joueur.pos)
        current_pnj = None
        for pnj in pnjs:
            pnj_pos = pygame.Vector2(pnj.pos)
            if joueur_pos.distance_to(pnj_pos) < 20:
                current_pnj = pnj

        if current_pnj:
            button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
            draw_button(screen, "Interagir", button_pos, 140, 40, (0, 128, 0))

        pygame.display.flip()

    pygame.quit()

# Démarrage du jeu
if __name__ == "__main__":
    main()
