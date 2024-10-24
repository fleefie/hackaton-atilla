from entitee import Entitee

class Pnj(Entitee):
    def __init__(self, pos: tuple[int, int], nom: str, desc: str, stats: dict, dialogue: str):
        super().__init__(pos, nom, desc, stats)
        self.dialogue = dialogue

    def interaction(self):
        # Afficher la boite de dialogue
        print(self.nom)
        print(self.description)
        print(self.dialogue) # TODO CHANGE ME
        if self.statistiques["vendeur"] == True:
            # Afficher l'interface de vente
            for obj in self.inventaire:
                print(obj) # TODO CHANGE ME
