class Pnj:
    def __init__(self, metier: str, niveau: int):
        self.metier = metier  
        self.inventaire = []  # Liste des objets que le PNJ possède
        self.niveau = niveau  # Niveau du PNJ

    def afficher_inventaire(self):
        """Affiche tous les objets dans l'inventaire du PNJ."""
        if not self.inventaire:
            print("L'inventaire est vide.")
        else:
            print("Inventaire du PNJ :")
            for objet in self.inventaire:
                print(f"- {objet}")

    def vendre_objets(self):
        """Vendre des objets en fonction du métier du PNJ."""
        if self.metier == "Armurier":
            self.inventaire = ["Armure légère", "Armure en acier", "Bouclier"]
            print(f"{self.metier} vend des armures : {', '.join(self.inventaire)}.")
        elif self.metier == "Forgeron":
            self.inventaire = ["Épée", "Hache", "Dague"]
            print(f"{self.metier} vend des armes : {', '.join(self.inventaire)}.")
        elif self.metier == "Alchimiste":
            self.inventaire = ["Potion de soin", "Potion de mana", "Potion de force"]
            print(f"{self.metier} vend des potions : {', '.join(self.inventaire)}.")
        else:
            print(f"{self.metier} n'a rien à vendre.")


    def __str__(self):
        """Renvoie une représentation sous forme de chaîne de caractères du PNJ."""
        inventaire_str = ", ".join(self.inventaire) if self.inventaire else "Aucun objet"
        return (f"PNJ : {self.metier}\n"
                f"Niveau : {self.niveau}\n"
                f"Inventaire : {inventaire_str}")
