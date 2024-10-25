# Good luck
# Have fun
# They'll pay for the back surgery for such a carry
#                   - Belle of Foxes
#                           - Made by Fleefie
#                             Because life is a bitch, and then you die

from objet import Objet
from objet import Potion
from objet import Livre
from objet import Arme
from objet import Armure

def check_entree(msg, type_attendu=None, valeurs_attendues=None):
    while True:
        entree = input(msg).strip()

        if type_attendu:
            try:
                entree = type_attendu(entree)
            except ValueError:
                print(f"Erreur, on attends un {type_attendu.__name__}.")
                continue

        if valeurs_attendues and entree not in valeurs_attendues:
            print(f"Erreur, les valeurs attendues sont: {', '.join(map(str, valeurs_attendues))}")
            continue

        return entree

def game_start():
    # Création

    def menu_boucle():
               
        print("Étape 1: création des objets")
        nmbr = 0
        objets = []
        while True:
            print(f"Vous avez créé {nmbr} objets. Souhaitez-vous afficher ces objets [1], en créer un nouveau [2], ou en supprimer un? [3]")
            match check_entree("", int, [1, 2, 3]):
                case 1:
                    for obj in objets:
                        print(f"{obj}")
                case 2:
                    nom = check_entree("Nom ?", str)
                    description = check_entree("Description ?", str)
                    prix = check_entree("Prix ?", int)
                    rarete = check_entree("Rareté? [commun, peu commun, rare, epique, legendaire]", str, \
                            ["commun", "peu commun", "rare", "epique", "legendaire"])
                    minint = check_entree("Intelligence minimale ?", int)
                    minstr = check_entree("Force minimale ?", int)
                    encombat = check_entree("Utilisable en combat ?", bool)
                    match check_entree("Type d'objet ? [arme, armure, potion, livre, autre]", str, ["arme", "armure", "potion", "livre", "autre"]):
                        case "arme":
                            degats = check_entree("Dégats de l'arme ?", int)
                            objets.append(Arme(nom, description, int(prix), rarete, int(minint), int(minstr), int(degats)))
                        case "armure":
                            resistance = check_entree("Résistance au dégats (multiplicateur) ?", float) 
                            objets.append(Armure(nom, description, int(prix), rarete, int(resistance), int(minint), int(minstr)))
                        case "potion":
                            objets.append(Potion(nom, description, int(prix), rarete, {"utilisable": True,"encombat": encombat,"consommable": True}))
                        case "livre":
                            typelivre = check_entree("Type de livre? [force, intelligence, hpmax]", str, ["force", "intelligence", "hpmax"])
                            objets.append(Livre(nom, description, int(prix), rarete, {"utilisable": True,"encombat": encombat,"consommable": True}, typelivre))
                        case "autre":
                            objets.append(Objet(nom, description, int(prix), rarete, {"utilisable": False, "encombat": False}, None))
                    print(f"Votre objet: {objets[nmbr]}")
                    nmbr += 1
                case 3:
                    ALAIDE = 1
                    for obj in objets:
                        print(f"{ALAIDE}: {obj}")
                        objets.pop(1 + int(check_entree("Choisissez-en un", int, range(1, nmbr+1, 1))))
                        nmbr -= 1
                        ALAIDE += 1
    menu_boucle()
game_start()
