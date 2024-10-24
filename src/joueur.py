class Joueur():
    def __init__(self, HP = 100, nom, race, classe, inventaire=[]):
        self.nom = nom
        self.race = race
        self.classe = classe
        self.inventaire = inventaire
        self.statistiques = {'HP_MAX' : 100,'force': 10,"intelligence" : 10, 'resistance' : 10 } #Stat de base à moduler 
        self.HP = HP
        
    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} :")
        for stat, valeur in self.statistiques.items():
            print(f"{stat.capitalize()} : {valeur}")

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{objet} ajouté à l'inventaire.")

    def utiliser_objet(self, objet):
        
        if objet in self.inventaire :
            if objet.nom == "potion" : 
                self.statistiques['HP'] += 20 * dict_rarete[objet.rarete]
                
            if objet.nom == ""
            