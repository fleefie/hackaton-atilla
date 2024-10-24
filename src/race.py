class Race:
    Type = { 
        "guerrier": "Noble Guerrier",
        "elfe": "Elfe Magique",
        "nain": "Nain Discret",
        "barbare": "Grand Barbare Combatant",
        "orc": "Puissant Orc",
        "erreur": "ERREUR: MAUVAIS TYPE"
    }


    """
    Défini une race

    Parameters:
        nom (str): Nom de la race
        description (str): Description courte de la race
        lore (str): Lore de la race
    """
    def __init__(self, nom: str, description: str, lore: str, type: str):
        self.nom = nom
        self.description = description
        self.lore = lore
        if type in self.Type:
            self.type = type
        else:
            self.type = "erreur"
