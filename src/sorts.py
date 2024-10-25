

"""class Sort():

    def __init__(self, p_nom: str, desc: str, mana: int, proprietes: dict, p_fn_utilisation):
        self.nom = p_nom
        self.desc = desc
        self.mana = mana
        self.rarete = 1
        self.proprietes = proprietes
        self.utiliser = None
        if callable(p_fn_utilisation):
            self.utiliser = p_fn_utilisation """

class Sort():
    def __init__(self, p_nom: str, desc: str, mana: int, rarete: str, proprietes: dict, p_fn_utilisation):
        """
        Classe qui représente un sort magique.
        
        :param p_nom: Nom du sort
        :param desc: Description du sort
        :param mana: Coût en mana du sort
        :param rarete: Rarete du sort (commune, rare, épique, etc.)
        :param proprietes: Dictionnaire contenant les propriétés du sort (comme les dégâts)
        :param p_fn_utilisation: Fonction d'utilisation du sort (doit être callable)
        """
        self.nom = p_nom
        self.desc = desc
        self.mana = mana
        self.rarete = rarete
        self.proprietes = proprietes  # Propriétés comme les dégâts
        self.utiliser = None
        
        if callable(p_fn_utilisation):
            self.utiliser = p_fn_utilisation

def utiliser_sort(sort, liste_ent : list):
    for i in liste_ent:
        i.statistiques['hp'] -= sort.proprietes['degats']
        
        



