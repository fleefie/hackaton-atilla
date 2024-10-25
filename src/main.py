import pygame
from entitee import Entitee
from combat import Combat
from joueur import Joueur  # Classe Joueur héritée d'Entitee ou définie à part
from sorts import Sort  # Classe pour définir les sorts
from objet import Objet


def utiliser_eclair(sort, joueur, cible):
    # Applique des dégâts plus élevés à la cible
    cible.stats['hp'] -= sort.proprietes['degats']

# Fonctions d'utilisation des sorts
def utiliser_boule_de_feu(sort, joueur, cible):
    # Applique des dégâts à la cible
    cible.stats['hp'] -= sort.proprietes['degats']

# Fonction d'utilisation du sort


def main():
    pygame.init()
    
    # Créer la fenêtre de jeu
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Combat Pygame")

    # Créer les statistiques du joueur
    statistiques_joueur = {
        'hp': 100,
        'hpmax': 100,
        'mana': 50,
        'force': 10,
        'intelligence': 10
    }

    # Création des sorts du joueur (uniquement Boule de Feu et Éclair)
    sort1 = Sort(
        "Boule de Feu", 
        "Projette une boule de feu", 
        10, 
        "commune", 
        {'degats': 30}, 
        utiliser_boule_de_feu
    )

    sort3 = Sort(
        "Éclair", 
        "Frappe l'ennemi avec un éclair puissant", 
        15, 
        "rare", 
        {'degats': 45}, 
        utiliser_eclair
    )

    # Création du joueur avec les deux sorts
    joueur = Joueur((50, 50), "Héros", "Le protagoniste du jeu", statistiques_joueur, {})

    # Création des ennemis
    statistiques_ennemi = {
        'hp': 50,
        'hpmax': 50,
        'mana': 0,
        'force': 8,
        'intelligence': 0
    }
    ennemi1 = Entitee((300, 200), "Gobelin", "Un petit gobelin", statistiques_ennemi)
    ennemi2 = Entitee((400, 300), "Orque", "Un puissant orque", statistiques_ennemi)
    liste_entites = [ennemi1, ennemi2]

    # Lancement du combat
    combat = Combat(joueur, liste_entites)
    combat.commencer_combat(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
