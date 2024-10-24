Raretes = {
    "commun": 1,
    "peu commun": 2,
    "rare": 4,
    "epique": 8,
    "legendaire": 16
}

class Objet():

    def __init__(self, p_nom: str, desc: str, p_prix: int, p_rarete: str, p_consommable: bool, p_fn_utilisation):
        self.nom = p_nom
        self.desc = desc
        self.prix = p_prix
        self.rarete = 1
        if p_rarete in Raretes:
            self.rarete = Raretes[p_rarete] 
        self.consommable = p_consommable
        self.utiliser = None
        if callable(p_fn_utilisation):
            self.utiliser = p_fn_utilisation
    
    def __str__(self):
        return f"{self.nom} (Prix: {self.prix}, Rarete: {self.rarete})"


class Arme(Objet):
    def __init__(self, p_nom: str, desc: str, p_prix: int, p_rarete: str, p_restriction_intelligence: int, p_restriction_force: int, p_degat: int, p_dura: int):
        super().__init__(p_nom, desc, p_prix, p_rarete, False, None)
        self.restriction_mana = p_restriction_intelligence
        self.restriction_force = p_restriction_force
        self.degat = p_degat
        self.dura = p_dura
    
    def __str__(self):
        return f"{super().__str__()}, Degats: {self.degat}, Durabilite: {self.dura}, Restriction Mana: {self.restriction_mana}, Restriction Force: {self.restriction_force}"


class Armure(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, multiplicateur_degats: float, durabilite: int):
        super().__init__(nom, desc, prix, rarete, False, None)
        self.multiplicateur_degats = multiplicateur_degats
        self.durabilite = durabilite
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, Multiplicateur de dégâts: {self.multiplicateur_degats}, "
                f"Durabilité: {self.durabilite}")


def utiliser_potion(pot, ent):
    if "pv" in ent.statistiques:
        ent.statistiques["hp"] += 20 * Raretes[pot.rarete]
        if ent.statistiques["hp"] >= ent.statistiques["hpmax"]:
            ent.statistiques["hp"] = ent.statistiques["hpmax"]
    else:
        print("L'entitée n'as pas de PV!")

class Potion(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, consommable: bool):
        super().__init__(nom, desc, prix, rarete, consommable, utiliser_potion)
