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
from race import Race
from sorts import Sort
from sorts import utiliser_sort

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

        print("Étape 1: création des objets")
        nmbr = 0
        objets = []
        while True:
            print(f"Vous avez créé {nmbr} objets. Souhaitez-vous afficher ces objets [1], en créer un nouveau [2], ou en supprimer un? [3]. [0] pour quitter.")
            match check_entree("", int, [1, 2, 3, 0]):
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
                case 0:
                    break


        print("Étape 2: création des sorts")
        nmbr = 0
        sorts = []
        while True:
            print(f"Vous avez créé {nmbr} sorts. Souhaitez-vous afficher ces sorts [1], en créer un nouveau [2], ou en supprimer un? [3]. [0] pour quitter.")
            match check_entree("", int, [1, 2, 3, 0]):
                case 1:
                    for sort in sorts:
                        print(f"{sort}")
                case 2:
                    nom = check_entree("Nom ?", str)
                    description = check_entree("Description ?", str)
                    prix = check_entree("Prix ?", int)
                    rarete = check_entree("Rareté? [commun, peu commun, rare, epique, legendaire]", str, \
                            ["commun", "peu commun", "rare", "epique", "legendaire"])
                    maxcibles = check_entree("Cibles max?", int)
                    dmg = check_entree("Dégats?", int)
                    mana = check_entree("Mana?", int)
                    print(f"Votre sort: {sorts[nmbr]}")
                    sorts.append(Sort(nom, description, int(mana), rarete, {"maxcibles": maxcibles, "degats": dmg}, utiliser_sort))
                    nmbr += 1
                case 3:
                    ALAIDE = 1
                    for sort in sorts:
                        print(f"{ALAIDE}: {sort}")
                        sorts.pop(1 + int(check_entree("Choisissez-en un", int, range(1, nmbr+1, 1))))
                        nmbr -= 1
                        ALAIDE += 1
                case 0:
                    break


        print("Étape 3: création des races")
        nmbr = 0
        races = []
        while True:
            print(f"Vous avez créé {nmbr} races. Souhaitez-vous afficher ces races [1], en créer un nouvelle [2], ou en supprimer une? [3]. [0] pour quitter.")
            match check_entree("", int, [1, 2, 3, 0]):
                case 1:
                    for race in races:
                        print(f"{race}")
                case 2: 
                    nom = check_entree("Nom ?", str)
                    description = check_entree("Description courte ?", str)
                    desclongue = check_entree("Description longue ?", str)
                    stre = check_entree("Force ?", int)
                    intl = check_entree("Intelligence ?", int)
                    defn = check_entree("Defense ?", int)
                    sortsrace = []
                    for sort in sorts:
                        if check_entree(f"ajouter le sort {sort.nom} à la race ?", bool):
                            sortsrace.append(sort)

                    races.append(Race(nom, description, desclongue, {"force": stre, "intelligence": intl, "defense": defn}, sortsrace))
                    print(f"Votre race: {races[nmbr]}")
                    nmbr += 1
                case 3:
                    ALAIDE = 1
                    for race in races:
                        print(f"{ALAIDE}: {race}")
                        races.pop(1 + int(check_entree("Choisissez-en une", int, range(1, nmbr+1, 1))))
                        nmbr -= 1
                        ALAIDE += 1
                case 0:
                    break



        print("Étape 3: création des classes")
        nmbr = 0
        classes = []
        while True:
            print(f"Vous avez créé {nmbr} classes. Souhaitez-vous afficher ces classes [1], en créer une nouvelle [2], ou en supprimer une? [3]. [0] pour quitter.")
            match check_entree("", int, [1, 2, 3, 0]):
                case 1:
                    for classe in classes:
                        print(f"{race}")
                case 2: 
                    nom = check_entree("Nom ?", str)
                    description = check_entree("Description courte ?", str)
                    desclongue = check_entree("Description longue ?", str)
                    stre = check_entree("Force ?", int)
                    intl = check_entree("Intelligence ?", int)
                    defn = check_entree("Defense ?", int)
                    sortsclasse = []
                    for sort in sorts:
                        if check_entree(f"ajouter le sort {sort.nom} à la classe ?", bool):
                            sortsclasse.append(sort)

                    classes.append(Classe(nom, description, desclongue, {"force": stre, "intelligence": intl, "defense": defn}, sortsrace))
                    print(f"Votre race: {races[nmbr]}")
                    nmbr += 1
                case 3:
                    ALAIDE = 1
                    for race in races:
                        print(f"{ALAIDE}: {race}")
                        races.pop(1 + int(check_entree("Choisissez-en une", int, range(1, nmbr+1, 1))))
                        nmbr -= 1
                        ALAIDE += 1
                case 0:
                    break


        
    menu_boucle()
game_start()
