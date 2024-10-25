import pygame
from joueur import Joueur
from entitee import Entitee

class Combat:
    def __init__(self, joueur, liste_entites):
        self.liste_entites = liste_entites
        self.joueur = joueur
        self.tour = 1
        self.current_choice = 0  # Navigation in action menu
        self.current_target = 0  # Navigation in targets
        self.messages = []  # List of messages to display on screen

    def afficher_messages(self, screen):
        """Affiche les messages de combat dans la fenêtre."""
        font = pygame.font.Font(None, 36)
        for index, message in enumerate(self.messages):
            text = font.render(message, True, (0, 0, 0))
            screen.blit(text, (20, 200 + index * 30))

    def afficher_etat(self, screen):
        """Affiche l'état des entités après chaque tour sur la fenêtre."""
        font = pygame.font.Font(None, 36)
        screen.fill((255, 255, 255))  # Fond blanc

        # Afficher l'état du joueur
        joueur_text = font.render(
            f"{self.joueur.nom} - PV : {self.joueur.statistiques['hp']}/{self.joueur.statistiques['hpmax']}, Mana : {self.joueur.statistiques['mana']}", 
            True, 
            (0, 0, 0)
        )
        screen.blit(joueur_text, (20, 20))  # Display player's stats

        # Afficher l'état des adversaires
        for idx, entite in enumerate(self.liste_entites):
            if entite.est_vivant():
                text = font.render(f"{entite.nom} - PV : {entite.statistiques['hp']}/{entite.statistiques['hpmax']}", True, (0, 0, 0))
            else:
                text = font.render(f"{entite.nom} est mort.", True, (150, 0, 0))
            screen.blit(text, (20, 60 + idx * 30))

        self.afficher_messages(screen)  # Afficher les messages après l'état des entités
        pygame.display.flip()  # Met à jour l'affichage

    def afficher_actions(self, screen):
        """Affiche les options d'action pour le joueur."""
        font = pygame.font.Font(None, 36)
        actions = ["Attaquer", "Utiliser un sort", "Utiliser un objet (non implémenté)", "S'enfuir"]

        screen.fill((255, 255, 255))  # Fond blanc

        for index, action in enumerate(actions):
            if index == self.current_choice:
                text = font.render(f"> {action}", True, (0, 0, 255))
            else:
                text = font.render(action, True, (0, 0, 0))
            screen.blit(text, (20, 100 + index * 40))

        self.afficher_messages(screen)  # Affiche les messages en bas
        pygame.display.flip()  # Met à jour l'affichage

    def afficher_cibles(self, screen):
        """Affiche les cibles disponibles pour l'attaque ou l'utilisation d'un sort."""
        font = pygame.font.Font(None, 36)
        screen.fill((255, 255, 255))  # Fond blanc

        text = font.render("Cibles disponibles :", True, (0, 0, 0))
        screen.blit(text, (20, 200))

        cibles_vivantes = [ent for ent in self.liste_entites if ent.est_vivant()]
        for index, cible in enumerate(cibles_vivantes):
            if index == self.current_target:
                text = font.render(f"> {cible.nom} (PV : {cible.statistiques['hp']})", True, (0, 0, 255))
            else:
                text = font.render(f"{cible.nom} (PV : {cible.statistiques['hp']})", True, (0, 0, 0))
            screen.blit(text, (40, 240 + index * 30))

        self.afficher_messages(screen)  # Affiche les messages en bas
        pygame.display.flip()  # Met à jour l'affichage

    def afficher_sorts(self, screen):
        """Affiche les sorts disponibles pour le joueur."""
        font = pygame.font.Font(None, 36)
        screen.fill((255, 255, 255))  # Fond blanc

        # Affiche le titre "Sorts disponibles :"
        titre = font.render("Sorts disponibles :", True, (0, 0, 0))
        screen.blit(titre, (20, 200))

        # Affiche les sorts du joueur avec une surbrillance pour le choix actuel
        for index, sort in enumerate(self.joueur.lore):
            if index == self.current_choice:
                text = font.render(f"> {sort.nom} (Mana : {sort.mana})", True, (0, 0, 255))
            else:
                text = font.render(f"{sort.nom} (Mana : {sort.mana})", True, (0, 0, 0))
            screen.blit(text, (40, 240 + index * 30))

        # Affiche les messages en bas
        self.afficher_messages(screen)
        pygame.display.flip()  # Met à jour l'affichage


    def ajouter_message(self, message):
        """Ajoute un message à la liste des messages à afficher."""
        self.messages.append(message)
        if len(self.messages) > 5:  # Limite le nombre de messages affichés
            self.messages.pop(0)  # Remove the oldest message

    def tour_entites(self):
        """Gère le tour des ennemis, qui attaquent le joueur."""
        for entite in self.liste_entites:
            if entite.est_vivant():
                cible = self.joueur
                self.ajouter_message(f"{entite.nom} attaque {cible.nom} !")
                entite.attaquer(cible)  # Chaque entité attaque uniquement le joueur
                if not self.joueur.est_vivant():
                    self.ajouter_message(f"{self.joueur.nom} a été vaincu !")
                    return False
        return True

    def tour_de_combat(self, screen):
        """Gère un tour complet de combat."""
        action = self.process_choice(screen)

        if action == 'fuir':
            self.ajouter_message(f"{self.joueur.nom} a réussi à fuir ! Le combat est terminé.")
            return False

        # Vérifier si toutes les entités ennemies sont mortes
        if all(not e.est_vivant() for e in self.liste_entites):
            self.ajouter_message(f"{self.joueur.nom} a remporté le combat après {self.tour} tours !")
            return False

        # Tour des entités (ennemis)
        if not self.tour_entites():
            return False

        # Affichage de l'état après chaque tour
        self.afficher_etat(screen)
        self.tour += 1
        return True
    
    def choisir_objet_inventaire(self, screen):
        """Affiche l'inventaire du joueur pour sélectionner un objet et le retourne."""
        font = pygame.font.Font(None, 36)
        current_choice = 0  # Position de l'objet sélectionné
        running = True
        objet_choisi = None

        while running:
            screen.fill((255, 255, 255))  # Fond blanc

            # Vérifier si l'inventaire est vide
            if not self.joueur.inventaire:
                text = font.render("Votre inventaire est vide.", True, (0, 0, 0))
                screen.blit(text, (20, 100))
                pygame.display.flip()
                pygame.time.wait(2000)  # Pause de 2 secondes
                return None  # Sortir et retourner None si inventaire vide

            # Afficher chaque objet de l'inventaire
            for index, objet in enumerate(self.joueur.inventaire):
                if index == current_choice:
                    text = font.render(f"> {objet.nom}", True, (0, 0, 255))  # Objet sélectionné
                else:
                    text = font.render(objet.nom, True, (0, 0, 0))  # Autres objets
                screen.blit(text, (20, 100 + index * 40))

            pygame.display.flip()

            # Gérer la navigation et la sélection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if current_choice > 0:
                            current_choice -= 1
                    elif event.key == pygame.K_DOWN:
                        current_choice = (current_choice + 1) % len(self.joueur.inventaire)
                    elif event.key == pygame.K_RETURN:
                        objet_choisi = self.joueur.inventaire[current_choice]
                        running = False  # Fin de la sélection

        return objet_choisi

    

    def commencer_combat(self, screen):
        """Commence le combat et continue jusqu'à ce qu'il n'y ait plus de participants."""
        
        running = True
        while self.joueur.est_vivant() and any(e.est_vivant() for e in self.liste_entites) and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.current_choice > 0:
                            self.current_choice -= 1  # Navigation vers le haut dans les actions
                        else:
                            self.current_choice = 3  # Boucle vers la dernière option
                    elif event.key == pygame.K_DOWN:
                        self.current_choice = (self.current_choice + 1) % 4  # Navigation vers le bas dans les actions
                    elif event.key == pygame.K_RETURN:
                        action = self.process_choice(screen)
                        if action == 'attaquer':
                            self.afficher_cibles(screen)  # Affiche les cibles si l'action nécessite une cible
                            self.selectionner_cible(screen)  # Gérer la sélection de cible
                        elif action == 'utiliser_objet':
                            objet = self.choisir_objet_inventaire(screen)  # Affiche et récupère l'objet choisi
                            if objet:
                                objet.utiliser(self.joueur)  # Utiliser l'objet si un choix est fait
                                self.joueur.inventaire.remove(objet)  # Retire l'objet de l'inventaire après utilisation
                                self.afficher_etat(screen)  # Actualiser l'état après l'utilisation de l'objet
                            
                        elif action == 'utiliser_sort':
                            self.afficher_sorts(screen)  # Affiche les sorts si l'action nécessite un choix
                            self.selectionner_sort(screen)  # Gérer la sélection de sort
                        elif action == 'fuir':
                            self.ajouter_message(f"{self.joueur.nom} a réussi à fuir ! Le combat est terminé.")
                            running = False
                        else:
                            self.tour_entites()  # Après l'action du joueur, les entités attaquent
                            self.afficher_etat(screen)  # Afficher l'état des entités

            # Affiche les actions du joueur à chaque itération
            self.afficher_actions(screen)

        if self.joueur.est_vivant():
            self.ajouter_message(f"{self.joueur.nom} a survécu et remporté le combat !")
        else:
            self.ajouter_message("Le joueur a été vaincu.")

    def process_choice(self, screen):
        """Traite le choix du joueur."""
        screen.fill((255, 255, 255))
        if self.current_choice == 0:  # Attaquer
            return 'attaquer'
        elif self.current_choice == 1:  # Utiliser un sort
            return 'utiliser_sort'
        elif self.current_choice == 2:  # Utiliser un objet
            return 'utiliser_objet'
        elif self.current_choice == 3:  # Fuir
            return 'fuir'

    def selectionner_cible(self, screen):
        """Gère la sélection d'une cible à attaquer."""
        running = True
        # Remplir l'écran
        screen.fill((255, 255, 255))
            
            # Afficher l'état des entités
        self.afficher_etat(screen)
            
            # Afficher les actions
        self.afficher_actions(screen)
            
            # Rafraîchir l'affichage
        pygame.display.flip()

        running = True
        cibles_vivantes = [ent for ent in self.liste_entites if ent.est_vivant()]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.current_target > 0:
                            self.current_target -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_target = (self.current_target + 1) % len(cibles_vivantes)
                    elif event.key == pygame.K_RETURN:
                        cible = cibles_vivantes[self.current_target]
                        self.joueur.attaquer(cible)  # Joueur attaque la cible sélectionnée
                        self.ajouter_message(f"{self.joueur.nom} attaque {cible.nom} !")
                        if not cible.est_vivant():
                            self.ajouter_message(f"{cible.nom} est vaincu !")
                        running = False  # Terminer la sélection de cible

            self.afficher_cibles(screen)

    def selectionner_sort(self, screen):
        """Gère la sélection d'un sort à utiliser."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.current_choice > 0:
                            self.current_choice -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_choice = (self.current_choice + 1) % len(self.joueur.sorts)
                    elif event.key == pygame.K_RETURN:
                        sort = self.joueur.sorts[self.current_choice]
                        if self.joueur.statistiques['mana'] >= sort.mana:
                            self.joueur.utiliser_sort(sort)
                            self.ajouter_message(f"{self.joueur.nom} utilise {sort.nom} !")
                        else:
                            self.ajouter_message(f"{self.joueur.nom} n'a pas assez de mana pour utiliser {sort.nom}.")
                        running = False  # Terminer la sélection de sort

            self.afficher_sorts(screen)