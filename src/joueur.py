from entitee import Entitee
from sorts import Sort


"""
Représente notre joueur!
"""
class Joueur(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, description: str, statistiques: dict, lore: dict):
        super().__init__(pos, nom, description, statistiques)
    
        self.lore = lore
        self.sorts = []
    def __str__(self):
        return f"{self.nom} est à la case {self.pos}, on le connaît pour {self.description},\
    ses statistiques sont : {self.statistiques}, \
        lore : {self.lore} "
    
    
    """
    Ajoute ``sort`` à l'inventaire des sorts
    """
    def ajouter_sort(self, sort: Sort):
        self.sorts.append(sort)




