from abc import ABC, abstractmethod
from objet import Objet

class Entitee(ABC):
    """
    Défini une entitée. Cette classe est une classe de base et est censée
    être héritée.
    """

    @abstractmethod
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


    def ajouter_inventaire(obj: Objet):
        pass

    def utiliser_objet(self, nom: str):
        for obj in self.inventaire:
            if type(obj) != Objet:
                raise NotImplementedError("Un non-objet est dans l'inventaire!")
            if obj.nom == nom:
                indice = self.inventaire.index(obj)
                self.inventaire[indice].utiliser()
                if self.inventaire[indice].estConsommable:
                    self.inventaire.pop(indice)
