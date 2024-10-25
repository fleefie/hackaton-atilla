from entitee import Entitee
import pygame


class Pnj(Entitee):
    """
    Défini un PNJ. Si il possède "vendeur": true dans ses statistiques, il sera
    capable de vendre son inventaire.

    Paramètres:
        - (x, y): position sur la carte
        - nom: Nom du PNJ
        - desc: Description du PNJ.
        - stats: statistiques du PNJ.
        - dialogue: string contenant le dialogue de bienvenue du PNJ
        - sprite_path: lien vers le sprite
    """
    def __init__(self, pos: tuple[int, int], nom: str, desc: str, stats: dict, dialogue: str, sprite_path: str):
        super().__init__(pos, nom, desc, stats)
        self.dialogue = dialogue
        self.sprite = pygame.image.load(sprite_path).convert_alpha()  # Charger le sprite du PNJ

    
    def __str__(self):
        return f"{self.nom} est un PNJ, à la position {self.pos}.\n Ses statistiques sont: {self.statistiques}, dialogue : {self.dialogue}"
    

    """
    Dessine le PNJ sur la surface ``surface``
    """
    def draw(self, surface):
        surface.blit(self.sprite, self.pos)

    def interaction(self, ent):
        # Afficher la boîte de dialogue
        print(self.nom)
        print(self.description)
        print(self.dialogue)  # TODO CHANGE ME
        if self.statistiques.get("vendeur", False):
            # Afficher l'interface de vente
            for obj in self.inventaire:
                print(obj)  # TODO CHANGE ME


"""
Permet à ``joueur`` d'acheter ``objet`` à ``pnj``
"""
def achat(joueur, pnj, objet):
    
    if joueur.statistiques['argent'] < objet.prix : 
        print(f"pas assez d'argent pour acheter {objet}")
    else : 
        joueur.statistiques['argent'] -= objet.prix
        pnj.statistiques['argent'] += objet.prix
        pnj.inventaire.remove(objet)
        joueur.inventaire.append(objet)


"""
Pas mal, non? C'est francais.
"""
def vente(joueur, pnj, objet ):
    achat(pnj, joueur, objet)
