import random
from entitee import Entitee

class Combat:
    def __init__(self, liste_entites):
        """Initialise un combat avec plusieurs entités."""
        self.liste_entites = liste_entites  # Stocke la liste des entités participant au combat
        self.tour = 1  # Initialise le compteur de tours

    def afficher_etat(self):
        """Affiche l'état de chaque entité."""
        print("\nÉtat des entités :")
        for entite in self.liste_entites:
            print(f"{entite.race} - PV : {entite.hp}")

    def tour_de_combat(self):
        """Effectue un tour de combat où chaque entité attaque une autre."""
        print(f"\n--- Tour {self.tour} ---")

        for entite in self.liste_entites:
            if entite.est_vivant():
                # Choisir une cible au hasard parmi les autres entités
                cible = self.choisir_cible(entite)
                if cible:
                    entite.attaquer(cible)

        # Affiche l'état de toutes les entités après chaque tour
        self.afficher_etat()
        self.tour += 1

    def choisir_cible(self, attaquant):
        """Choisit une cible vivante au hasard parmi les autres entités."""
        entites_vivantes = [e for e in self.liste_entites if e.est_vivant() and e != attaquant]
        if entites_vivantes:
            return random.choice(entites_vivantes)  # Choisit une cible au hasard
        return None
    
    def est_vivant(self):
        return self.hp > 0  # Retourne True si les points de vie sont supérieurs à 0, sinon False


    def commencer_combat(self):
        """Commence le combat et gère les tours jusqu'à ce qu'il ne reste qu'une seule entité en vie."""
        print("Le combat commence !")
        
        # Continue le combat tant qu'il reste plus d'une entité vivante
        while len([e for e in self.liste_entites if e.est_vivant()]) > 1:
            self.tour_de_combat()

        # Affiche le vainqueur
        survivants = [e for e in self.liste_entites if e.est_vivant()]
        if len(survivants) == 1:
            print(f"\n{survivants[0].race} a remporté le combat après {self.tour - 1} tours !")
        elif len(survivants) == 0:
            print("\nTous les combattants sont morts.")


