class Creature:
    def __init__(self, race: str, force: int, mana: int, hp: int, resistance: int):
        #Construction de la classe créature
        self.race = race  
        self.force = force  
        self.mana = mana  #mana corresponds à un niveau d'habilité pour pouvoir porter une arme
        self.hp = hp 
        self.resistance = resistance  
        self.inventaire = [] 


