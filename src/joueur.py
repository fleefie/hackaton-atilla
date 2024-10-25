from entitee import Entitee
from sorts import Sort

class Joueur(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, description: str, statistiques: dict, lore: dict):
        super().__init__(pos, nom, description, statistiques)
    
        self.lore = lore
        self.sorts = []
    def __str__(self):
        return f"{self.nom} est à la case {self.pos}, on le connaît pour {self.description},\
    ses statistiques sont : {self.statistiques}, \
        lore : {self.lore} "
    
    
    
    
    def ajouter_sort(self, sort: Sort):
        self.sorts.append(sort)

    def utiliser_sort(self, nom: str, cible: Entitee):
        indice = 0
        for sort in self.sorts:
            if sort.nom == nom:
                self.sorts[indice].utiliser(self.sorts[indice], cible)
            indice += 1

