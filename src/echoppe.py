from entitee import Pnj

class Echoppe:
    def __init__(self, nom: str, pnj: Pnj, pos: tuple[int, int]):
        """
        Constructeur pour Echoppe

        Parameters:
            nom (str): Nom de l'échoppe
            pnj (Pnj): PNJ associé
            pos (int, int): Position en (x, y) sur la carte
        """
        self.nom = nom
        self.pnj = pnj
        self.pos = pos
