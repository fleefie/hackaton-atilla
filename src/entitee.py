from objet import Objet

class Entitee:
    """
    Défini une entitée. Cette classe est une classe de base et est censée
    être héritée.
    """

    def interaction(self):
        """
        Est censée être écrasée par sa classe héritée!
        """
        raise NotImplementedError("La sous-classe doit implémenter une interaction")

    def __init__(self, pos: tuple[int, int], nom: str, description: str, statistiques : dict):
        self.pos = pos
        self.nom = nom
        self.description = description
        self.inventaire = []
        self.statistiques = {'HP_MAX' : 100,'force': 10,"intelligence" : 10, 'resistance' : 10 } #Stat de base à moduler 


    def ajouter_inventaire(self, obj: Objet):
        self.inventaire.append(obj)

    def utiliser_objet(self, nom: str):
        indice = 0
        for obj in self.inventaire:
            if obj.nom == nom:
                self.inventaire[indice].utiliser(self.inventaire[indice], self)
                if self.inventaire[indice].consommable:
                    self.inventaire.pop(indice)
                break
            indice += 1
