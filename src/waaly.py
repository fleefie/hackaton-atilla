
# ajouter dans entitee


def attaquer(self, combat, cible):
        """Attaque une autre entité et réduit ses points de vie."""
        if self.est_vivant():
            # Calcul des dégâts (ici on utilise simplement la force de l'attaquant)
            degat = self.statistiques["force"]
            print(f"{self.nom} attaque {cible.nom} et inflige {degat} points de dégâts.")
            cible.statistiques["hp"] -= degat


