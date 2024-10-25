Raretes = {
    "commun": 1,
    "peu commun": 2,
    "rare": 3,
    "epique": 4,
    "legendaire": 5
}


"""
Définit un objet. Cette classe en elle-même ne fait rien actuellement, mais peut
être implémentée du moment qu'une fonction est passé

Paramètres:
    - nom: nom de l'objet
    - desc: description de l'objet
    - prix: prix de l'objet pour les marchands
    - rarete: rareté de l'objet
    - proprietes: dictionnaire des propriétés
    - fn_utilisation: fonction associée à l'objet instantié.
"""
class Objet():
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict, fn_utilisation):
        self.nom = nom
        self.desc = desc
        self.prix = prix
        self.rarete = 1
        self.proprietes = proprietes
        if rarete in Raretes:
            self.rarete = Raretes[rarete] 
        self.utiliser = None
        if callable(fn_utilisation):
            self.utiliser = fn_utilisation
        else:
            self.utiliser = lambda: None
    
    def __str__(self):
        return f"{self.nom} (Prix: {self.prix}, Rarete: {self.rarete}, utilisable: {self.proprietes['utilisable']} (en combat? {self.proprietes['encombat']}))"


"""
Équipe l'objet ``obj`` pour l'entitée ``ent``.
C'est un simple wrapper pour ``ent.equiper``.
"""
def equiper_objet(obj, ent):
    ent.equiper(obj)


"""
Représente une arme, avec un niveau min d'int et de str pour être équipé
"""
class Arme(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, min_intelligence: int, min_force: int, degat: int):
        stats = {
                "consommable": False, 
                "utilisable": True, 
                "encombat": False, 
                "equipable": {
                    "armure": False, 
                    "arme": True
                    },
                "degats": degat, 
                "minintel": min_intelligence, 
                "minforce": min_force
                }
        super().__init__(nom, desc, prix, rarete, stats, equiper_objet)
    def __str__(self):
        return f"{self.nom}, armure avec {self.proprietes['degats']} de dégats. (Prix: {self.prix}, Rarete: {self.rarete}, utilisable: {self.proprietes['utilisable']} (en combat? {self.proprietes['encombat']}))"


"""
Représente une armure. Même logique que l'arme, avec une résistance
"""
class Armure(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, resistance: float, minintel: int, minforce: int):
        stats = { 
                 "consommable": False, 
                 "utilisable": True, 
                 "encombat": False, 
                 "equipable":  {
                     "armure": True, 
                     "arme": False
                     }, 
                 "resistance": resistance,
                 "minintel": minintel,
                 "minforce": minforce
                 }
        super().__init__(nom, desc, prix, rarete, stats, equiper_objet)
    def __str__(self):
        return f"{self.nom}, armure avec {self.proprietes['resistance']} de résistance. (Prix: {self.prix}, Rarete: {self.rarete}, utilisable: {self.proprietes['utilisable']} (en combat? {self.proprietes['encombat']}))"


"""
Fonction utilisée pour une potion
"""
def utiliser_potion(pot, ent):
    if "hp" in ent.statistiques:
        ent.statistiques["hp"] += 20 * 2**(pot.rarete-1)
        if ent.statistiques["hp"] >= ent.statistiques["hpmax"]:
            ent.statistiques["hp"] = ent.statistiques["hpmax"]

        print("Ca a marche lets go!")
    else:
        print("L'entitée n'as pas de PV!")


"""
Classe représentant la potion.
"""
class Potion(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_potion)


"""
Classe représenant un livre
"""
class Livre(Objet) :
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict, type_livre : str):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_livre)
        self.type_livre = type_livre


"""
Fonction utilisée pour un livre
"""
def utiliser_livre(livre,ent):
    if not livre.type_livre in ent.statistiques:
        print(f"l'entité n'a pas de {livre.type_livre}")
    if livre.type_livre == "force" :
        ent.statistiques["force"] += 5
    if livre.type_livre == "intelligence" :
        ent.statistiques["intelligence"] += 5
    if livre.type_livre == "hpmax" :
        ent.statistiques["hpmax"] += 3 
