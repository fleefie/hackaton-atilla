from sorts import Sort


"""
Défini une race

Parameters:
    nom (str): Nom de la race
    description (str): Description courte de la race
    lore (str): Lore de la race
"""
class Classe:
    def __init__(self, nom: str, description: str, desclongue: str, stats: dict, sorts: list[Sort]):
        self.nom = nom
        self.description = description
        self.desclongue = desclongue
        self.stats = stats
        self.sorts = sorts
