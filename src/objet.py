class Objet:
    def __init__(self, p_nom: str, p_prix: int, p_rarete: str):
        self.nom = p_nom
        self.prix = p_prix
        self.rarete = p_rarete
    
    def __str__(self):
        return f"{self.nom} (Prix: {self.prix}, Rarete: {self.rarete})"

class Arme(Objet):
    def __init__(self, p_nom: str, p_prix: int, p_rarete: str, p_restriction_intelligence: int, p_restriction_force: int, p_degat: int, p_dura: int):
        super().__init__(p_nom, p_prix, p_rarete)
        self.restriction_mana = p_restriction_intelligence
        self.restriction_force = p_restriction_force
        self.degat = p_degat
        self.dura = p_dura
    
    def __str__(self):
        return f"{super().__str__()}, Degats: {self.degat}, Durabilite: {self.dura}, Restriction Mana: {self.restriction_mana}, Restriction Force: {self.restriction_force}"

class Armure(Objet):
    def __init__(self, nom: str, prix: int, rarete: str, multiplicateur_degats: float, durabilite: int):
        super().__init__(nom, prix, rarete)
        self.multiplicateur_degats = multiplicateur_degats
        self.durabilite = durabilite
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, Multiplicateur de dégâts: {self.multiplicateur_degats}, "
                f"Durabilité: {self.durabilite}")


