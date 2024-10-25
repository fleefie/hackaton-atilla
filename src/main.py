import pygame
import pytmx
import os
from entitee import Entitee

# Configuration initiale de la carte et de l'affichage
TAILLE_CARTE = 960  # Taille totale de la carte (999x999)
TAILLE_ZONE = TAILLE_CARTE // 3  # Taille de chaque zone (320x320)

# Fonction principale du jeu
def main():
    pygame.init()

    # Taille de l'écran
    screen = pygame.display.set_mode((TAILLE_CARTE, TAILLE_CARTE))

    # Charger la carte Tiled
    print("Chemin actuel :", os.getcwd())
    tmx_data = pytmx.load_pygame("src/level_data/map.tmx")

    # Fonction pour dessiner la carte
    def draw_map(surface):
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    # Boucle de jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Dessiner la carte sur l'écran
        draw_map(screen)
        
        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()


# Démarrage du jeu
if __name__ == "__main__":
    main()
