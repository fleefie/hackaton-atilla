Raretes = {
    "commun": 1,
    "peu commun": 2,
    "rare": 3,
    "epique": 4,
    "legendaire": 5
}

class Objet():

    def __init__(self, p_nom: str, desc: str, p_prix: int, p_rarete: str, proprietes: dict, p_fn_utilisation):
        self.nom = p_nom
        self.desc = desc
        self.prix = p_prix
        self.rarete = 1
        self.proprietes = proprietes
        if p_rarete in Raretes:
            self.rarete = Raretes[p_rarete] 
        self.utiliser = None
        if callable(p_fn_utilisation):
            self.utiliser = p_fn_utilisation
        else:
            self.utiliser = lambda: None
    
    def __str__(self):
        return f"{self.nom} (Prix: {self.prix}, Rarete: {self.rarete}, utilisable: {self.proprietes['utilisable']} (en combat? {self.proprietes['encombat']}))"


def equiper_objet(obj, ent):
    ent.equiper(obj)

class Arme(Objet):
    def __init__(self, p_nom: str, desc: str, p_prix: int, p_rarete: str, p_min_intelligence: int, p_min_force: int, p_degat: int):
        stats = {
                "consommable": False, 
                "utilisable": True, 
                "encombat": False, 
                "equipable": {
                    "armure": False, 
                    "arme": True
                    },
                "degats": p_degat, 
                "minintel": p_min_intelligence, 
                "minforce": p_min_force
                }
        super().__init__(p_nom, desc, p_prix, p_rarete, stats, equiper_objet)

class Armure(Objet):
    def __init__(self, nom: str, desc: str, p_prix: int, p_rarete: str, p_resistance: float, minintel: int, minforce: int):
        stats = { 
                 "consommable": False, 
                 "utilisable": True, 
                 "encombat": False, 
                 "equipable":  {
                     "armure": True, 
                     "arme": False
                     }, 
                 "resistance": p_resistance,
                 "minintel": minintel,
                 "minforce": minforce
                 }
        super().__init__(nom, desc, p_prix, p_rarete, stats, equiper_objet)


def utiliser_potion(pot, ent):
    if "hp" in ent.statistiques:
        ent.statistiques["hp"] += 20 * 2**(pot.rarete-1)
        if ent.statistiques["hp"] >= ent.statistiques["hpmax"]:
            ent.statistiques["hp"] = ent.statistiques["hpmax"]
    else:
        print("L'entitée n'as pas de PV!")

class Potion(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_potion)
        
class Livre(Objet) :
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict, type_livre : str):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_livre)
        self.type_livre = type_livre
        
def utiliser_livre(livre,ent):
    if not livre.type_livre in ent.statistiques:
        print(f"l'entité n'a pas de {livre.type_livre}")
    if livre.type_livre == "force" :
        ent.statistiques["force"] += 5
    if livre.type_livre == "intelligence" :
        ent.statistiques["intelligence"] += 5
    if livre.type_livre == "hpmax" :
        ent.statistiques["hpmax"] += 3 
