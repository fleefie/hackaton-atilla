class Joueur():
    def __init__(self, nom, race, classe, niveau=1, inventaire=None, compétences=None):
        self.nom = nom
        self.race = race
        self.classe = classe
        self.niveau = niveau
        self.inventaire = inventaire if inventaire is not None else []
        self.compétences = compétences if compétences is not None else {}
        self.statistiques = {'force': 10,"intelligence" : 10 } #Stat de base à moduler 

    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} :")
        for stat, valeur in self.statistiques.items():
            print(f"{stat.capitalize()} : {valeur}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire.")

    def utiliser_compétence(self, compétence):
        if compétence in self.compétences:
            print(f"{self.nom} utilise la compétence {compétence}!")
        else:
            print(f"{self.nom} ne possède pas cette compétence.")

    def monter_niveau(self):
        self.niveau += 1
        print(f"{self.nom} a atteint le niveau {self.niveau}!")
        # Améliorer les statistiques à chaque niveau
        self.statistiques['force'] += 2
        self.statistiques['intelligence'] += 2