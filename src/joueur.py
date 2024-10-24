dict_rarete = {"commun" : 1, "peu commun"  : 2, "rare" : 4, "epic" : 8, "legendaire" : 16}



class Joueur():
    def __init__(self,entite , race :str, classe : str, HP = 100 ):
        self.entite = entite
        self.race = race
        self.classe = classe
        self.HP = HP
        
    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} :")
        for stat, valeur in self.statistiques.items():
            print(f"{stat.capitalize()} : {valeur}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire.")

