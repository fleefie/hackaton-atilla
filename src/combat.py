import random
from entitee import Entitee
from joueur import Joueur

class Combat:
    def __init__(self, joueur, liste_entites):
        """Initialise un combat avec plusieurs entités."""
        self.liste_entites = liste_entites  # Stocke la liste des entités participant au combat
        self.joueur = joueur
        self.tour = 1  # Initialise le compteur de tours

    def afficher_etat(self):
        """Affiche l'état de chaque entité."""
        print("\nÉtat des entités :")
        for entite in self.liste_entites:
            print(f"{entite.nom} - PV : {entite.hp}")

    def est_vivant(self, entite):
        """Vérifie si une entité est encore en vie."""
        return entite.hp > 0

    def obtenir_premiere_cible(self, attaquant):
        """Retourne la première entité vivante autre que l'attaquant."""
        for entite in self.liste_entites:
            if entite != attaquant and self.est_vivant(entite):
                return entite
        return None

    def tour_de_combat(self):
        """Effectue un tour de combat où chaque entité attaque une autre."""
        print(f"\n--- Tour {self.tour} ---")

        for entite in self.liste_entites:
            if self.est_vivant(entite):
                # Obtenir la première entité vivante autre que l'attaquant
                cible = self.obtenir_premiere_cible(entite)
                if cible:
                    entite.attaquer(cible)  # Appel de la méthode attaquer de l'entité

        # Affiche l'état de toutes les entités après chaque tour
        self.afficher_etat()
        self.tour += 1

    def commencer_combat(self):
        """Commence le combat et gère les tours jusqu'à ce qu'il ne reste qu'une seule entité en vie."""
        print("Le combat commence !")
        
        # Continue le combat tant qu'il reste plus d'une entité vivante
        while len([e for e in self.liste_entites if self.est_vivant(e)]) > 1:
            self.tour_de_combat()

        # Affiche le vainqueur
        survivants = [e for e in self.liste_entites if self.est_vivant(e)]
        if len(survivants) == 1:
            print(f"\n{survivants[0].nom} a remporté le combat après {self.tour - 1} tours !")
        elif len(survivants) == 0:
            print("\nTous les combattants sont morts.")
