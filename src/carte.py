from entitee import Entitee

"""
Classe représentant la carte. Elle est simplement composée d'une taille max
donnée par x et y, puis d'un tableau des entités.
"""
class Carte:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.entites = []

    def ajouter_entitee(self, ent: Entitee):
        self.entites.append(ent)
    
        
