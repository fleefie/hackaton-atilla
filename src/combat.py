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
            print("2. S'enfuir")
            choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour s'enfuir) : ")

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