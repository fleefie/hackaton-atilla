from entitee import Entitee
import random

class Carte:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.entites = []

    def ajouter_entitee(self, ent: Entitee):
        self.entites.append(ent)
    
        