
# ajouter dans entitee


def attaquer(self, combat, cible):
        """Attaque une autre entité et réduit ses points de vie."""
        if self.est_vivant():
            # Calcul des dégâts (ici on utilise simplement la force de l'attaquant)
            degats = self.force
            print(f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts.")
            cible.recevoir_degats(degats)