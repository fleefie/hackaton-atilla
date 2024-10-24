from entitee import Entitee
dict_rarete = {"commun" : 1, "peu commun"  : 2, "rare" : 4, "epic" : 8, "legendaire" : 16}



class Joueur(Entitee):
    def __init__(self,entite , race :str, classe : str, HP = 100, pos: tuple[int, int], nom: str, description: str, statistiques : dict):
        super().__init__(pos, nom, description, statistiques, inventaire, statistiques)

        
    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} :")
        for stat, valeur in self.statistiques.items():
            print(f"{stat.capitalize()} : {valeur}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire.")

