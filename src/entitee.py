from objet import Objet


"""
Défini une entitée. Cette classe est une classe de base et est censée
être héritée.

Paramètres:
    - (x, y): position
    - nom
    - description
    - statistiques
"""
class Entitee:

    def interaction(self, joueur):
        """
        Est censée être écrasée par sa classe héritée!
        """
        raise NotImplementedError("La sous-classe doit implémenter une interaction")

    def __init__(self, pos: tuple[int, int], nom: str, description: str, statistiques : dict):
        self.pos = pos
        self.nom = nom
        self.description = description
        self.statistiques = statistiques
        self.inventaire = []
        self.statistiques = statistiques
        self.equipement = {}


    def ajouter_inventaire(self, obj: Objet):
        self.inventaire.append(obj)


    def __str__(self) :
        return "Cette entité est magique et ne peut pas être dans le monde réel \
                Elle est étrange, et les dieux de ce monde ont probablement fait une \
                immense erreur si vous parvenez à l'observer. \
            https://www.youtube.com/watch?v=dQw4w9WgXcQ"


    def retirer_inventaire(self, nom: str):
        indice = 0
        for obj in self.inventaire:
            if obj.nom == nom:
                self.inventaire.pop(indice)


    def utiliser_objet(self, nom: str):
        indice = 0
        for obj in self.inventaire:
            if obj.nom == nom:
                self.inventaire[indice].utiliser(self.inventaire[indice], self)
                if self.inventaire[indice].proprietes["consommable"]:
                    self.inventaire.pop(indice)
                break
            indice += 1


    def equiper(self, obj: Objet):
        if "equipable" in obj.proprietes:
            if obj.proprietes["equipable"]["armure"]:
                if "armure" in self.equipement:
                    self.ajouter_inventaire(self.equipement["armure"])
                self.equipement["armure"] = obj
                self.retirer_inventaire(obj.nom)
                self.statistiques["resistance"] = obj.proprietes["resistance"]
            if obj.proprietes["equipable"]["arme"]:
                if "arme" in self.equipement:
                    self.ajouter_inventaire(self.equipement["arme"])
                self.equipement["arme"] = obj
                self.retirer_inventaire(obj.nom)
                self.statistiques["degats"] = obj.proprietes["degats"]


    def est_vivant(self):
        """Vérifie si l'entité est encore vivante."""
        return self.statistiques['hp'] > 0
    
    def attaquer(self, cible):
        """L'entité attaque une autre entité."""
        degats = self.statistiques['force']
        cible.statistiques['hp'] -= degats
        if cible.statistiques['hp'] < 0:
            cible.statistiques['hp'] = 0
        print(f"{self.nom} attaque {cible.nom} pour {degats} dégâts !")
