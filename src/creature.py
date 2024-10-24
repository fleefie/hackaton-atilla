class Creature:
    def __init__(self, race: str, force: int, mana: int, hp: int, resistance: int):
        self.race = race  # Race du personnage (par ex: Humain, Orc, Elfe)
        self.force = force  # Force du personnage, affecte les dégâts physiques
        self.mana = mana  # Mana, capacité à utiliser des armes magiques
        self.hp = hp  # Points de vie (santé)
        self.resistance = resistance  # Résistance physique du personnage
        self.inventaire = []  # Liste d'armes/objets dans l'inventaire