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
    print("Chemin actuel :", os.getcwd())
    tmx_data = pytmx.load_pygame("src/level_data/map.tmx")

    # Charger les textures
    player_texture = pygame.image.load("sprites/fHero.png").convert_alpha()
    player_texture = pygame.transform.scale(player_texture, (16, 16))

    creature_sprites = {
        "Goblin": pygame.image.load("sprites/goblin.png").convert_alpha(),
        "Dragon": pygame.image.load("sprites/dragon.png").convert_alpha(),
    }
    statistiques_joueur = {
            'hp': 100,
            'hpmax': 100,
            'mana': 50,
            'force': 10,
            'intelligence': 10
        }
    # Initialiser le joueur et les créatures
    joueur = Joueur([TAILLE_CARTE // 2, TAILLE_CARTE // 2], "Lucas", "Guerrier", statistiques_joueur,{})


       statistiques_ennemi = {
        'hp': 50,
        'hpmax': 50,
        'mana': 0,
        'force': 8,
        'intelligence': 0
    }
 
def __init__(self, pos: tuple[int, int], nom: str, desc: str, stats: dict, lore: dict):
    creatures = [
        Creature((random.randint(0, TAILLE_CARTE - 50), random.randint(0, TAILLE_CARTE - 50)),
                 "Goblin", "Une créature agile", {"hp": 30, "mana": 0, "force": 10, "resistance": 5}, {"race": "Goblin", "classe": "Monstre"}),
        Creature((random.randint(0, TAILLE_CARTE - 50), random.randint(0, TAILLE_CARTE - 50)),
                 "Dragon", "Un monstre imposant", {"hp": 200, "mana": 50, "force": 40, "resistance": 25}, {"race": "Dragon", "classe": "Boss"})
    ]

    pnjs = [
        Pnj((384, 406), "Forgeron", "Un marchand amical", {"vendeur": True, "argent": 50}, "Bonjour ! Que puis-je faire pour vous ?", "sprites/shrek.png"),
        Pnj((560, 406), "Armurier", "Un guide mystérieux", {"vendeur": True}, "Bienvenue dans notre monde !", "sprites/knight.png"),
        Pnj((384, 566), "Alchimiste", "Un vieux bougre", {"vendeur": True}, "Les secrets de cette terre sont puissants.", "sprites/necromancer.png")
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
    current_creature = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Vérifier si le joueur interagit avec un PNJ
                if current_pnj:
                    button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
                    button_rect = pygame.Rect(button_pos[0], button_pos[1], 140, 40)
                    if button_rect.collidepoint(mouse_pos):
                        current_pnj.interaction(joueur)

                # Vérifier si le joueur interagit avec une créature
                if current_creature:
                    button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 100)
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
        current_creature = None

        # Vérification de la proximité avec les PNJs
        for pnj in pnjs:
            pnj_pos = pygame.Vector2(pnj.pos)
            if joueur_pos.distance_to(pnj_pos) < 20:
                current_pnj = pnj

        # Vérification de la proximité avec les créatures
        for creature in creatures:
            creature_pos = pygame.Vector2(creature.pos)
            if joueur_pos.distance_to(creature_pos) < 20:
                current_creature = creature

        # Afficher le bouton d'interaction avec les PNJs ou les créatures
        if current_pnj:
            button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 50)
            draw_button(screen, "Interagir", button_pos, 140, 40, (0, 128, 0))

        if current_creature:
            button_pos = (TAILLE_CARTE - 150, TAILLE_CARTE - 100)
            draw_button(screen, "Combattre", button_pos, 140, 40, (128, 0, 0))

        pygame.display.flip()

    pygame.quit()

# Démarrage du jeu
if __name__ == "__main__":
    main()
