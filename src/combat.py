
# Classe Combat corrigée
class Combat:
    def __init__(self, joueur, liste_entites):
        self.liste_entites = liste_entites
        self.joueur = joueur
        self.tour = 1

    def afficher_etat(self):
        """Affiche l'état des entités après chaque tour."""
        print("\nÉtat des entités :")
        print(f"{self.joueur.nom} - PV : {self.joueur.statistiques['hp']}/{self.joueur.statistiques['hpmax']}, Mana : {self.joueur.statistiques['mana']}")
        for entite in self.liste_entites:
            if entite.est_vivant():
                print(f"{entite.nom} - PV : {entite.statistiques['hp']}/{entite.statistiques['hpmax']}")
            else:
                print(f"{entite.nom} est mort.")

    def afficher_sorts(self):
        """Affiche les sorts disponibles pour le joueur."""
        print("\nSorts disponibles :")
        for index, sort in enumerate(self.joueur.sorts):
            print(f"{index + 1}. {sort.nom} (Mana : {sort.mana}, Description : {sort.desc})")




    def tour_joueur(self):
        """Gère le tour du joueur (attaque, sort, fuite, etc.)."""
        print(f"\n--- Tour {self.tour} : Tour du joueur {self.joueur.nom} ---")
        while True:
            print("\n1. Attaquer")
            print("2. Utiliser un sort")
            print("3. Utiliser un objet (non implémenté)")
            print("4. S'enfuir")
            choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour utiliser un sort, 3 pour utiliser un objet, 4 pour s'enfuir) : ")

            if choix == '1':
                # Attaque simple
                print("\nCibles disponibles :")
                cibles_vivantes = [ent for ent in self.liste_entites if ent.est_vivant()]
                for index, entite in enumerate(cibles_vivantes):
                    print(f"{index + 1}. {entite.nom} (PV: {entite.statistiques['hp']})")

                # Sélection d'une cible
                try:
                    cible_choisie = int(input("Choisissez une cible à attaquer : ")) - 1
                    cible = cibles_vivantes[cible_choisie]
                    
                    # Attaque seulement la cible choisie
                    self.joueur.attaquer(cible)
                    
                except (IndexError, ValueError):
                    print("Cible invalide. Essayez de nouveau.")
                    continue
                break
            elif choix == '2':
                # Utiliser un sort
                self.afficher_sorts()
                try:
                    sort_choisi = int(input("Choisissez un sort à utiliser : ")) - 1
                    sort = self.joueur.sorts[sort_choisi]

                    # Cibles disponibles pour les sorts
                    cibles_vivantes = [ent for ent in self.liste_entites if ent.est_vivant()]
                    print("\nCibles disponibles :")
                    for index, entite in enumerate(cibles_vivantes):
                        print(f"{index + 1}. {entite.nom} (PV: {entite.statistiques['hp']})")

                    # Sélection d'une cible pour le sort
                    cible_choisie = int(input("Choisissez une cible pour le sort : ")) - 1
                    cible = cibles_vivantes[cible_choisie]

                    # Utilisation du sort sur la cible
                    self.joueur.utiliser_sort(sort.nom, cible)
                except (IndexError, ValueError):
                    print("Choix invalide, réessayez.")
                    continue
                break

            elif choix == '3':
                print("Utilisation d'objets non implémentée.")
                break

            elif choix == '4':
                print(f"{self.joueur.nom} tente de s'enfuir !")
                return 'fuir'

            else:
                print("Choix invalide. Veuillez choisir à nouveau.")

        return 'attaquer'

    def tour_entites(self):
        """Gère le tour des ennemis, qui attaquent le joueur."""
        for entite in self.liste_entites:
            if entite.est_vivant():
                cible = self.joueur
                print(f"{entite.nom} attaque {cible.nom} !")
                entite.attaquer(cible)  # Chaque entité attaque uniquement le joueur
                if not self.joueur.est_vivant():
                    print(f"{self.joueur.nom} a été vaincu !")
                    return False
        return True

    def tour_de_combat(self):
        """Gère un tour complet de combat."""
        print(f"\n--- Tour {self.tour} ---")
        action = self.tour_joueur()

        if action == 'fuir':
            print(f"{self.joueur.nom} a réussi à fuir ! Le combat est terminé.")
            return False

        # Vérifier si toutes les entités ennemies sont mortes
        if all(not e.est_vivant() for e in self.liste_entites):
            print(f"\n{self.joueur.nom} a remporté le combat après {self.tour} tours !")
            return False

        # Tour des entités (ennemis)
        if not self.tour_entites():
            return False

        # Affichage de l'état après chaque tour
        self.afficher_etat()
        self.tour += 1
        return True

    def commencer_combat(self):
        """Commence le combat et continue jusqu'à ce qu'il n'y ait plus de participants."""
        print("Le combat commence !")
        while self.joueur.est_vivant() and any(e.est_vivant() for e in self.liste_entites):
            if not self.tour_de_combat():
                break

        if self.joueur.est_vivant():
            print(f"\n{self.joueur.nom} a survécu et remporté le combat !")
        else:
            print("\nLe joueur a été vaincu.")
