from entitee import Entitee
from objet import Objet

class Pnj(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, description: str):
        super().__init__(pos, nom, description)
        self.inventaire = []
    
    def interaction(self):
        return 0

