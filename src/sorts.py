"""
Classe qui représente un sort magique.

Paramètres:
    - nom: Nom du sort
    - desc: Description du sort
    - mana: Coût en mana du sort
    - rarete: Rarete du sort (commune, rare, épique, etc.)
    - proprietes: Dictionnaire contenant les propriétés du sort (comme les dégâts)
    - fn_utilisation: Fonction d'utilisation du sort (doit être callable)
"""
class Sort():
    def __init__(self, nom: str, desc: str, mana: int, rarete: str, proprietes: dict):

        self.nom = nom
        self.desc = desc
        self.mana = mana
        self.rarete = rarete
        self.proprietes = proprietes  # Propriétés comme les dégâts
        
        
        def __str__(self) : 
            return f"{self.nom}, sort de rareté {rarete}, qui coute {mana} de mana pour {self.proprietes['degats']}"
    
    def utiliser(self, sort, liste_ent : list):
        for i in liste_ent:
            i.statistiques['hp'] -= sort.proprietes['degats']

"""
Fonction par défaut du sort.
TODO: Implémenter différentes fonctions pour différent types de sorts?
"""

