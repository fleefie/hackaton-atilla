class Region:
    def __init__(self, nom :str, type_lieu : str, topographie : str, population : list, position : tuple):
        self.nom = nom
        self.type_lieu = type_lieu  # Ex: Ville, Forêt, Désert
        self.topographie = topographie  # Ex: Montagneuse, Plate
        self.population = population
        self.position = position  # tuple de tuple de coordonnée qui délimite la zone 

    def afficher_informations(self):
        print(f"Région : {self.nom}")
        print(f"Type de lieu : {self.type_lieu}")
        print(f"Topographie : {self.topographie}")
        print(f"Population : {self.population}")
        print(f"Position : {self.position}")

    def ajouter_habitant(self, habitant):
        self.population.append(habitant)
        print(f"{habitant} ajouté à la population de {self.nom}.")
