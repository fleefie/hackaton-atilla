from entitee import Entitee

class Creature(Entitee):
    def __init__(self, race: str, force: int, degat: int, inteligence: int, hp: int, resistance: int):
        #Construction de la classe créature
        self.race = race  
        self.force = force  
        self.inteligence = inteligence  #mana corresponds à un niveau d'habilité pour pouvoir porter une arme
        self.hp = hp 
        self.degat = degat
        self.resistance = resistance  
        self.inventaire = []

    def attaquer(self, cible):
        """La créature attaque une autre créature (cible)."""
        degats_infliges = self.degat*cible.resistance
        degats_infliges = max(0, degats_infliges)  
        # Les dégâts ne peuvent pas être négatifs
        cible.hp -= degats_infliges
        print(f"{self.race} attaque {cible.race} et inflige {degats_infliges} dégâts.")
        print(f"{cible.race} a maintenant {cible.hp} points de vie restants.")
        
        if cible.hp <= 0:
            print(f"{cible.race} est mort !")
            cible.hp = 0

    def est_vivant(self):
        """Vérifie si la créature est toujours en vie."""
        return self.hp > 0

    def combat(self, adversaire):
        """Simule un combat entre cette créature et un adversaire."""
        print(f"Le combat commence entre {self.race} et {adversaire.race} !")
        
        tour = 1
        while self.est_vivant() and adversaire.est_vivant():
            print(f"\n--- Tour {tour} ---")
            
            # La créature actuelle attaque l'adversaire
            self.attaquer(adversaire)
            
            # Si l'adversaire est toujours vivant, il contre-attaque
            if adversaire.est_vivant():
                adversaire.attaquer(self)
            
            tour += 1

        if self.est_vivant():
            print(f"{self.race} a gagné le combat !")
        else:
            print(f"{adversaire.race} a gagné le combat !")    


    def __str__(self): #fonction pour afficher
        """Renvoie une représentation sous forme de chaîne de caractères du personnage."""
        inventaire_str = ", ".join([arme['nom'] for arme in self.inventaire]) if self.inventaire else "Aucun objet"
        return (f"Personnage : {self.race}\n"
                f"Force : {self.force}\n"
                f"Mana : {self.mana}\n"
                f"Points de vie : {self.hp}\n"
                f"Résistance : {self.resistance}\n"
                f"Inventaire : {inventaire_str}")

