import pygame
import random
from entitee import Entitee

# Configuration initiale de la carte et de l'affichage
TAILLE_CARTE = 999  # Taille totale de la carte (999x999)
TAILLE_ZONE = TAILLE_CARTE // 3  # Taille de chaque zone (333x333)

class Carte:
    def __init__(self):
        self.entites = []  # Liste des entités à placer sur la carte

    def ajouter_entitee(self, ent: Entitee):
        """Ajoute une entité sur la carte."""
        self.entites.append(ent)

    def afficher_carte(self, screen):
        """Affiche la carte divisée en 9 zones avec des couleurs différentes et les entités en noir."""
        # Couleurs des 9 zones
        couleurs = [
            (200, 0, 0), (0, 200, 0), (0, 0, 200),
            (200, 200, 0), (200, 0, 200), (0, 200, 200),
            (150, 100, 50), (100, 150, 50), (50, 100, 150)
        ]
        
        # Dessiner les 9 zones
        for row in range(3):
            for col in range(3):
                couleur = couleurs[row * 3 + col]
                pygame.draw.rect(screen, couleur, (col * TAILLE_ZONE, row * TAILLE_ZONE, TAILLE_ZONE, TAILLE_ZONE))

        # Dessiner les entités (en noir)
        for ent in self.entites:
            pygame.draw.circle(screen, (0, 0, 0), ent.pos, 5)  # Les entités sont représentées par des cercles noirs


# Fonction principale du jeu
def main():
    pygame.init()

    # Créer la fenêtre de jeu
    screen = pygame.display.set_mode((TAILLE_CARTE, TAILLE_CARTE))
    pygame.display.set_caption("Carte de Jeu avec Entités")

    # Création de la carte et des entités
    carte = Carte()
    

    # Ajouter des entités aléatoires avec des statistiques
    for i in range(100):  # Exemple avec 10 entités
        pos = (random.randint(0, TAILLE_CARTE - 1), random.randint(0, TAILLE_CARTE - 1))  # Position aléatoire
        nom = f"Entitee_{i}"  # Nom unique pour chaque entité
        description = "Une créature mystérieuse"  # Exemple de description
        statistiques = {
            'hp': 100,  # Points de vie de base
            'hpmax': 100,
            'force': random.randint(5, 15),
            'intelligence': random.randint(5, 15)
        }
        ent = Entitee(pos, nom, description, statistiques)  # Créer une entité avec les arguments corrects
        carte.ajouter_entitee(ent)

    # Boucle principale du jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Remplir l'écran (fond)
        screen.fill((255, 255, 255))  # Blanc

        # Afficher la carte avec les zones et les entités
        carte.afficher_carte(screen)

        # Mettre à jour l'affichage
        pygame.display.flip()

    pygame.quit()


# Démarrage du jeu
if __name__ == "__main__":
    main()
