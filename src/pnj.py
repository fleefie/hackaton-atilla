from entitee import Entitee
from objet import Armure
from joueur import Joueur

class Pnj(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, desc: str, stats: dict, dialogue: str):
        super().__init__(pos, nom, desc, stats)
        self.dialogue = dialogue

    def interaction(self,ent):
        # Afficher la boite de dialogue
        print(self.nom)
        print(self.description)
        print(self.dialogue) # TODO CHANGE ME
        if self.statistiques["vendeur"] == True:
            # Afficher l'interface de vente
            for obj in self.inventaire:
                print(obj) # TODO CHANGE ME
    
def achat(joueur, pnj, objet):
    
    if joueur.statistiques['argent'] < objet.prix : 
        print(f"pas assez d'argent pour acheter {objet}")
    else : 
        joueur.statistiques['argent'] -= objet.prix
        pnj.statistiques['argent'] += objet.prix
        pnj.inventaire.remove(objet)
        joueur.inventaire.append(objet)
    
def vente(joueur, pnj, objet ):
    achat(pnj, joueur, objet)
    
"""

joueur = Entitee((0, 0), "nomdel'ent", "une desc", {})
pnj = Pnj((0,0), "Didier", "maçon",{}, "cc")
pnj.statistiques['argent'] = 110
joueur.statistiques['argent'] = 100
objet = Armure("Grosse Armure jsp", "elle est bien big", 70, "rare", 0.8)
objet.prix = 110
pnj.inventaire.append(objet)

achat(joueur,pnj ,objet)
print("inventaire du joueur",joueur.inventaire)
print(joueur.statistiques['argent'])

"""
