from entitee import Entitee
from joueur import Joueur
from combat import Combat
import random

class Creature(Entitee):
    def __init__(self, race: str, hp: int, resistance: int):
        #Construction de la classe créature
        self.race = race  
        self.hp = hp 
        self.resistance = resistance  

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
        return (f"Personnage : {self.race}\n"
                f"Force : {self.force}\n"
                f"Mana : {self.mana}\n"
                f"Points de vie : {self.hp}\n"
                f"Résistance : {self.resistance}\n"
                f"Inventaire : {inventaire_str}")

"""        
creature = Creature("goblin,", 100, 0.5)
joueur = Joueur((100,100), "lucas", "test", {},"test")

creature.interaction(joueur)
"""
