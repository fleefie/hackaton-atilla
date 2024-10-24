class Competance:
    """
    Défini une compétance

    Parameters:
        nom (str): Nom de la compétance
        description (str): Description
        mana (int): Coût d'utilisation
        delai (int): Cooldown en tours
        processus (func): fonction exécutée lors de l'utilisation de la compétance
    """
    def __init__(self, nom: str, description: str, mana: float, delai: int, processus: function):
        self.nom = nom
        self.description = description
        self.mana = mana
        self.delai = delai
        if callable(processus):
            self.processus = processus
