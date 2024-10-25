import pygame
import pytmx
import os
import random
from entitee import Entitee
from creature import Creature
from joueur import Joueur
from pnj import Pnj
from combat import Combat

# Configuration initiale
TAILLE_CARTE = 960
VITESSE_JOUEUR = 0.8

# Fonction pour dessiner un bouton
def draw_button(surface, text, pos, width, height, color):
    pygame.draw.rect(surface, color, (pos[0], pos[1], width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(pos[0] + width // 2, pos[1] + height // 2))
    surface.blit(text_surface, text_rect)

# Fonction principale
def main():
    pygame.init()
    screen = pygame.display.set_mode((TAILLE_CARTE, TAILLE_CARTE))
    tmx_data = pytmx.load_pygame("src/level_data/map.tmx")

    # Charger les textures
    player_texture = pygame.image.load("sprites/fHero.png").convert_alpha()
    player_texture = pygame.transform.scale(player_texture, (16, 16))

    creature_sprites = {
        "Goblin": pygame.image.load("sprites/goblin.png").convert_alpha(),
        "Dragon": pygame.image.load("sprites/dragon.png").convert_alpha(),
        "Demon": pygame.image.load("sprites/demon.png").convert_alpha(),
        "Ghost": pygame.image.load("sprites/ghost.png").convert_alpha(),
        "Goblinking": pygame.image.load("sprites/goblinKing.png").convert_alpha(),
        "Orc": pygame.image.load("sprites/orc.png").convert_alpha(),
        "Skeleton": pygame.image.load("sprites/skeleton.png").convert_alpha(),
        "Slime": pygame.image.load("sprites/slime.png").convert_alpha(),
    }

    # Définir les zones de spawn pour chaque créature
    spawn_zones = {
        "Goblin": ((330, 650), (630, 950)),
        "Dragon": ((10, 650), (310, 950)),
        "Demon": ((10, 330), (310, 640)),
        "Ghost": ((10, 10), (310, 310)),
        "Goblinking": ((330, 10), (630, 310)),
        "Orc": ((650, 10), (950, 310)),
        "Skeleton": ((650, 330), (950, 630)),
        "Slime": ((650, 650), (950, 950)),
    }

    statistiques_joueur = {
        'hp': 100,
        'hpmax': 100,
        'mana': 50,
        'force': 10,
        'intelligence': 10
    }

    # Définir les zones de spawn pour chaque créature
    spawn_zones = {
        "Goblin": ((330, 650), (630, 950)),
        "Dragon": ((10, 650), (310, 950)),
        "Demon": ((10, 330), (310, 640)),
        "Ghost": ((10, 10), (310, 310)),
        "Goblinking": ((330, 10), (630, 310)),
        "Orc": ((650, 10), (950, 310)),
        "Skeleton": ((650, 330), (950, 630)),
        "Slime": ((650, 650), (950, 950)),
    }

    statistiques_joueur = {
        'hp': 100,
        'hpmax': 100,
        'mana': 50,
        'force': 10,
        'intelligence': 10
    }

    statistiques_ennemi = {
        'hp': 50,
        'hpmax': 50,
        'mana': 0,
        'force': 8,
        'intelligence': 0
    }
    # Initialiser le joueur et les créatures
    joueur = Joueur([TAILLE_CARTE // 2, TAILLE_CARTE // 2], "Lucas", "Guerrier", statistiques_joueur, {})

    # Initialiser les créatures avec des positions aléatoires dans leurs zones
    creatures = []
    for creature_name, ((x1, y1), (x2, y2)) in spawn_zones.items():
        pos = (random.randint(x1, x2), random.randint(y1, y2))
        creature = Creature(pos, creature_name, "Une créature", {"hp": 30,'hpmax':30, "mana": 0, "force": 10, "resistance": 5}, {"race": creature_name, "classe": "Monstre"})
        creatures.append(creature)

    # Initialiser les PNJ
    pnjs = [
        Pnj((384, 406), "Forgeron", "Un marchand amical", {"vendeur": True, "argent": 50}, "Bonjour ! Je vends du shit !!", "sprites/shrek.png"),
        Pnj((560, 406), "Armurier", "Un guide mystérieux", {"vendeur": True}, "Besoin d'un protège couilles ?", "sprites/knight.png"),
        Pnj((384, 566), "Alchimiste", "Un vieux bougre", {"vendeur": True}, "Un petit champipi ?", "sprites/necromancer.png")
    ]

    def draw_map(surface):
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    def draw_creatures(surface):
        for creature in creatures:
            sprite = creature_sprites.get(creature.nom)
            if sprite:
                surface.blit(sprite, creature.pos)

    def draw_joueur(surface, joueur):
        surface.blit(player_texture, joueur.pos)

    def draw_pnjs(surface):
        for pnj in pnjs:
            pnj.draw(surface)

    # Boucle de jeu
    running = True
    current_pnj = None
    current_creature = None  # Ajout d'une variable pour suivre la créature actuelle
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if current_pnj:
                    button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
                    button_rect = pygame.Rect(button_pos[0], button_pos[1], 140, 40)
                    if button_rect.collidepoint(mouse_pos):
                        current_pnj.interaction(joueur)

                if current_creature:
                    button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 100)  # Position du bouton "Combattre"
                    button_rect = pygame.Rect(button_pos[0], button_pos[1], 140, 40)
                    if button_rect.collidepoint(mouse_pos):
                        combat = Combat(joueur, [current_creature])
                        combat.commencer_combat(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            joueur.pos[1] -= VITESSE_JOUEUR
        if keys[pygame.K_s]:
            joueur.pos[1] += VITESSE_JOUEUR
        if keys[pygame.K_q]:
            joueur.pos[0] -= VITESSE_JOUEUR
        if keys[pygame.K_d]:
            joueur.pos[0] += VITESSE_JOUEUR

        joueur.pos[0] = max(0, min(joueur.pos[0], TAILLE_CARTE - 16))
        joueur.pos[1] = max(0, min(joueur.pos[1], TAILLE_CARTE - 16))

        draw_map(screen)
        draw_creatures(screen)
        draw_joueur(screen, joueur)
        draw_pnjs(screen)

        joueur_pos = pygame.Vector2(joueur.pos)
        current_pnj = None
        current_creature = None  # Réinitialisation à chaque boucle
        for pnj in pnjs:
            pnj_pos = pygame.Vector2(pnj.pos)
            if joueur_pos.distance_to(pnj_pos) < 20:
                current_pnj = pnj

        for creature in creatures:
            creature_pos = pygame.Vector2(creature.pos)
            if joueur_pos.distance_to(creature_pos) < 20:
                current_creature = creature

        # Affichage des boutons d'interaction
        if current_pnj:
            button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
            draw_button(screen, "Interagir", button_pos, 140, 40, (0, 128, 0))

        if current_creature:
            button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 100)  # Position du bouton "Combattre"
            draw_button(screen, "Combattre", button_pos, 140, 40, (255, 0, 0))  # Couleur du bouton "Combattre" en rouge

        pygame.display.flip()

    pygame.quit()

# Démarrage du jeu
if __name__ == "__main__":
    main()