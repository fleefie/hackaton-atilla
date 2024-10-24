from entitee import Entitee

class Creature(Entitee):
    def __init__(self, race: str, hp: int, resistance: int):
        #Construction de la classe créature
        self.race = race  
        self.hp = hp 
        self.resistance = resistance  



    def __str__(self): #fonction pour afficher
        """Renvoie une représentation sous forme de chaîne de caractères du personnage."""
        inventaire_str = ", ".join([arme['nom'] for arme in self.inventaire]) if self.inventaire else "Aucun objet"
        return (f"Personnage : {self.race}\n"
                f"Force : {self.force}\n"
                f"Mana : {self.mana}\n"
                f"Points de vie : {self.hp}\n"
                f"Résistance : {self.resistance}\n"
                f"Inventaire : {inventaire_str}")

