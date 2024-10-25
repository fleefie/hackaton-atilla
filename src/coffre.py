from entitee import Entitee


class Coffre(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, description: str, statistiques: dict, lore: dict):
        super().__init__(pos, nom, description, statistiques)
    
    def __str__(self):
        return f"{self.nom} est un très joli coffre "
    
    def interaction(self, ent): 
        print(self.nom)
        print(self.description)
        if len(self.inventaire) == 0 : print('coffre vide')
        else :
            print(self.inventaire)
            ent.inventaire += self.inventaire
            print("Vous avez récupéré le contenu du coffre ")
                
    