

import random

class Joueur:
    def __init__(self, nom, hp, attaque):
        self.nom = nom
        self.hp = hp
        self.attaque = attaque
        self.inventaire = []  # Initialisation de l'inventaire

    def attaquer(self, cible):
        """Attaque une cible et réduit ses points de vie."""
        print(f"{self.nom} attaque {cible.nom} pour {self.attaque} dégâts !")
        cible.hp -= self.attaque
        if cible.hp < 0:
            cible.hp = 0  # Évite les HP négatifs
        print(f"{cible.nom} a maintenant {cible.hp} PV.")

    def est_vivant(self):
        """Vérifie si le joueur est encore en vie."""
        return self.hp > 0

    def ajouter_objet(self, objet):
        """Ajoute un objet à l'inventaire."""
        self.inventaire.append(objet)

    def afficher_inventaire(self):
        """Affiche l'inventaire du joueur."""
        print("\nInventaire :")
        if not self.inventaire:
            print("L'inventaire est vide.")
        for index, objet in enumerate(self.inventaire):
            print(f"{index + 1}. {objet}")

class Entitee:
    def __init__(self, nom, hp, attaque):
        self.nom = nom
        self.hp = hp
        self.attaque = attaque

    def attaquer(self, cible):
        """Attaque une cible et réduit ses points de vie."""
        print(f"{self.nom} attaque {cible.nom} pour {self.attaque} dégâts !")
        cible.hp -= self.attaque
        if cible.hp < 0:
            cible.hp = 0  # Évite les HP négatifs
        print(f"{cible.nom} a maintenant {cible.hp} PV.")

    def est_vivant(self):
        """Vérifie si l'entité est encore en vie."""
        return self.hp > 0


class Objet:
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
    
    def __str__(self):
        return f"{self.nom} (Prix: {self.prix}, Rarete: {self.rarete})"


class Arme(Objet):
    def __init__(self, p_nom: str, desc: str, p_prix: int, p_rarete: str, p_min_intelligence: int, p_min_force: int, p_degat: int, p_dura: int):
        super().__init__(p_nom, desc, p_prix, p_rarete, {"consommable": False, "utilisable": True, "encombat": False}, None)
        self.restriction_mana = p_min_intelligence
        self.restriction_force = p_min_force
        self.degat = p_degat
        self.dura = p_dura
    
    def __str__(self):
        return f"{super().__str__()}, Degats: {self.degat}, Durabilite: {self.dura}, Restriction Mana: {self.restriction_mana}, Restriction Force: {self.restriction_force}"


class Armure(Objet):
    def __init__(self, nom: str, desc: str, p_prix: int, p_rarete: str, p_resistance: float, p_dura: int):
        super().__init__(nom, desc, p_prix, p_rarete, {"consommable": False, "utilisable": True, "encombat": False}, None)
        self.multiplicateur_degats = p_resistance
        self.durabilite = p_dura
    
    def __str__(self) -> str:
        return (f"{super().__str__()}, Multiplicateur de dégâts: {self.multiplicateur_degats}, "
                f"Durabilité: {self.durabilite}")


def utiliser_potion(pot, ent):
    if "pv" in ent.statistiques:
        ent.statistiques["hp"] += 20 * 2**(Raretes[pot.rarete]-1)
        if ent.statistiques["hp"] >= ent.statistiques["hpmax"]:
            ent.statistiques["hp"] = ent.statistiques["hpmax"]
    else:
        print("L'entitée n'as pas de PV!")

class Potion(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_potion)


class Livre(Objet):
    def __init__(self, nom: str, desc: str, prix: int, rarete: str, proprietes: dict, type_livre: str):
        super().__init__(nom, desc, prix, rarete, proprietes, utiliser_livre)
        self.type_livre = type_livre

def utiliser_livre(livre, ent):
    if not livre.type_livre in ent.statistiques:
        print(f"L'entité n'a pas de {livre.type_livre}")
    if livre.type_livre == "force":
        ent.statistiques["force"] += 5
    if livre.type_livre == "intelligence":
        ent.statistiques["intelligence"] += 5
    if livre.type_livre == "hpmax":
        ent.statistiques["hpmax"] += 3 


class Combat:
    def __init__(self, joueur, liste_entites):
        """Initialise un combat avec plusieurs entités."""
        self.liste_entites = liste_entites  # Stocke la liste des entités participant au combat
        self.joueur = joueur
        self.tour = 1  # Initialise le compteur de tours

    def afficher_etat(self):
        """Affiche l'état de chaque entité."""
        print("\nÉtat des entités :")
        print(f"{self.joueur.nom} - PV : {self.joueur.hp}")
        for entite in self.liste_entites:
            print(f"{entite.nom} - PV : {entite.hp}")

    def tour_joueur(self):
        """Gère le tour du joueur."""
        print(f"\n--- Tour {self.tour} : Tour du joueur {self.joueur.nom} ---")
        
        # Affichage des options pour le joueur
        while True:
            print("\n1. Attaquer")
            print("2. Utiliser un objet")
            print("3. S'enfuir")
            choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour utiliser un objet, 3 pour s'enfuir) : ")

            if choix == '1':
                # Si le joueur choisit d'attaquer
                print("\nCibles disponibles :")
                for index, entite in enumerate(self.liste_entites):
                    if entite.est_vivant():
                        print(f"{index + 1}. {entite.nom} (PV: {entite.hp})")

                # Le joueur choisit une cible
                while True:
                    try:
                        cible_choisie = int(input("Choisissez une cible à attaquer (entrez un numéro) : ")) - 1
                        if 0 <= cible_choisie < len(self.liste_entites) and self.liste_entites[cible_choisie].est_vivant():
                            cible = self.liste_entites[cible_choisie]
                            self.joueur.attaquer(cible)  # Le joueur attaque la cible choisie
                            break
                        else:
                            print("Choix invalide ou cible déjà morte.")
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
                break  # Sortie du choix d'action du joueur

            elif choix == '2':
                # Si le joueur choisit d'utiliser un objet
                self.joueur.afficher_inventaire()
                if self.joueur.inventaire:
                    while True:
                        try:
                            objet_choisi = int(input("Choisissez un objet à utiliser (entrez un numéro) : ")) - 1
                            if 0 <= objet_choisi < len(self.joueur.inventaire):
                                objet = self.joueur.inventaire[objet_choisi]
                                # Utiliser l'objet sur le joueur
                                objet.utiliser(objet, self.joueur)
                                print(f"{self.joueur.nom} a utilisé {objet.nom}.")
                                # Suppression de l'objet si c'est un consommable
                                if objet.proprietes.get("consommable"):
                                    self.joueur.inventaire.pop(objet_choisi)
                                break
                            else:
                                print("Choix invalide.")
                        except ValueError:
                            print("Veuillez entrer un numéro valide.")
                else:
                    print("Votre inventaire est vide.")
                break  # Sortie du choix d'action du joueur

            elif choix == '3':
                # Si le joueur choisit de s'enfuir
                print(f"{self.joueur.nom} tente de s'enfuir !")
                return 'fuir'  # Indique que le joueur a fui
            else:
                print("Choix invalide, veuillez recommencer.")

        return 'attaquer'  # Si le joueur attaque, continue le combat

    def tour_entites(self):
        """Gère le tour des autres entités (ennemis)."""
        for entite in self.liste_entites:
            if entite.est_vivant():
                cible = self.joueur  # Les entités attaquent le joueur
                print(f"{entite.nom} attaque {cible.nom} !")
                entite.attaquer(cible)  # L'entité attaque le joueur
                if not self.joueur.est_vivant():
                    print(f"{self.joueur.nom} a été vaincu !")
                    return False  # Si le joueur est mort, on arrête le combat
        return True

    def tour_de_combat(self):
        """Gère un tour de combat complet."""
        print(f"\n--- Tour {self.tour} ---")

        # Tour du joueur
        action = self.tour_joueur()

        if action == 'fuir':
            # Si le joueur tente de fuir
            print(f"{self.joueur.nom} a réussi à fuir ! Le combat est terminé.")
            return False  # Le joueur a fui, donc on arrête le combat

        # Vérification après l'attaque du joueur
        if len([e for e in self.liste_entites if e.est_vivant()]) == 0:
            print(f"\n{self.joueur.nom} a remporté le combat après {self.tour} tours !")
            return False  # Le combat est terminé, le joueur a gagné

        # Tour des entités (ennemis)
        if not self.tour_entites():
            return False  # Le combat est terminé, le joueur a perdu

        # Afficher l'état après chaque tour
        self.afficher_etat()
        self.tour += 1

        return True

    def commencer_combat(self):
        """Commence le combat et gère les tours jusqu'à ce qu'il ne reste qu'une seule entité en vie ou que le joueur s'enfuie."""
        print("Le combat commence !")
        
        # Continue le combat tant que le joueur est vivant et qu'il reste des ennemis
        while self.joueur.est_vivant() and len([e for e in self.liste_entites if e.est_vivant()]) > 0:
            if not self.tour_de_combat():
                break  # Arrête le combat si quelqu'un est mort ou que le joueur a fui

        # Vérification finale pour annoncer le gagnant ou la défaite
        if self.joueur.est_vivant():
            print(f"\n{self.joueur.nom} a survécu et remporté le combat !")
        else:
            print("\nLe joueur a été vaincu.")


# Exemple d'utilisation
Raretes = {'commune': 1, 'rare': 2, 'épique': 3}

# Création d'un joueur et d'entités
joueur = Joueur(nom="Héros", hp=100, attaque=10)
ennemi1 = Entitee(nom="Gobelin", hp=30, attaque=5)
ennemi2 = Entitee(nom="Orc", hp=50, attaque=8)

# Ajout d'objets à l'inventaire du joueur
potion = Potion(nom="Potion de soin", desc="Restaure 20 PV.", prix=10, rarete='commune', proprietes={"consommable": True})
joueur.ajouter_objet(potion)

# Lancement du combat
combat = Combat(joueur, [ennemi1, ennemi2])
combat.commencer_combat()
