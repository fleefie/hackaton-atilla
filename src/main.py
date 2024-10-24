from combat import Combat
#from competences import Competance
#from creature import Creature
#from echoppe import Echoppe
from joueur import Joueur
from entitee import Entitee
#from objet import Objet
#from pnj import Pnj
#from race import Race
#from region import Region
import pygame

dict_rarete = {"commun" : 1, "peu commun"  : 2, "rare" : 4, "epic" : 8, "legendaire" : 16}

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu de Rôle")
    clock = pygame.time.Clock()
    
    # Création d'un joueur
    joueur = Joueur(entite=(0, 0), race="Humain", classe="Guerrier")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        deplacement = (0, 0)

        if keys[pygame.K_z]:  # Z pour avancer (haut)
            deplacement = (0, -1)
        if keys[pygame.K_s]:  # S pour reculer (bas)
            deplacement = (0, 1)
        if keys[pygame.K_q]:  # Q pour aller à gauche
            deplacement = (-1, 0)
        if keys[pygame.K_d]:  # D pour aller à droite
            deplacement = (1, 0)

        if deplacement != (0, 0):
            joueur.deplacer(deplacement)

        # Exemple d'utilisation d'un objet
        if keys[pygame.K_e]:  # E pour utiliser un objet
            joueur.utiliser_objet("Potion de Vie")  # Remplace par un objet existant dans l'inventaire

        screen.fill((255, 255, 255))  # Efface l'écran
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
