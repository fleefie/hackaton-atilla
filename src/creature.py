from entitee import Entitee
from combat import Combat
import random

class Creature(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, desc: str, stats: dict, lore: dict):
        super().__init__(pos, nom, desc, stats)
        #Construction de la classe créature
        self.lore = lore

    def interaction(self, joueur):
        """Initialise et lance un combat entre le joueur et la créature."""
        # creer liste entre 1 et 3 mobs
        nbr_entites = random.randint(1, 3)
        liste_entites = [self for _ in range(nbr_entites)]
        
        # initialiser combat avec les entités
        combat = Combat(joueur, liste_entites)
        combat.commencer_combat()

    def __str__(self): #fonction pour afficher
        """Renvoie une représentation sous forme de chaîne de caractères du personnage."""
        inventaire_str = ", ".join([arme['nom'] for arme in self.inventaire]) if self.inventaire else "Aucun objet"
        return (f"Personnage : {self.lore['race']} {self.lore['classe']}\n"
                f"Force : {self.statistiques['force']}\n"
                f"Mana : {self.statistiques['mana']}\n"
                f"Points de vie : {self.statistiques['hp']}\n"
                f"Résistance : {self.statistiques['resistance']}\n"
                f"Inventaire : {inventaire_str}")

"""        
creature = Creature("goblin,", 100, 0.5)
joueur = Joueur((100,100), "lucas", "test", {},"test")

creature.interaction(joueur)
"""
