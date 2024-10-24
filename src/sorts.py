
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

def utiliser_eclair(sort, ent):
    """
    Cette fonction simule l'utilisation du sort 'éclair' sur une entité (ent).
    Elle inflige des dégâts en fonction de la puissance du sort.
    """
    degats_eclair = sort['degats']  # On récupère la valeur des dégâts de l'éclair depuis le sort
    print(f"{sort['nom']} inflige {degats_eclair} dégâts à {ent.nom}.")

    # Réduire les points de vie de l'entité
    ent.statistiques['hp'] -= degats_eclair

    # S'assurer que les HP ne sont pas négatifs
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher l'état de la cible après l'attaque
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")


class Eclair(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_eclair)

def utiliser_feu(sort, ent):
    """
    Cette fonction simule l'utilisation du sort 'feu' sur une entité (ent).
    Elle inflige des dégâts initiaux et applique éventuellement un effet de brûlure.
    """
    degats_feu = sort['degats']  # Dégâts immédiats du sort de feu
    brulure_duree = sort.get('brulure_duree', 0)  # Durée de la brûlure, si elle existe
    brulure_degats = sort.get('brulure_degats', 0)  # Dégâts de brûlure par tour, s'il y en a

    # Infliger les dégâts immédiats
    print(f"{sort['nom']} inflige {degats_feu} dégâts à {ent.nom}.")
    ent.statistiques['hp'] -= degats_feu

    # S'assurer que les HP ne tombent pas en dessous de 0
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher les PV après l'attaque initiale
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")

    # Appliquer l'effet de brûlure si disponible
    if brulure_duree > 0:
        print(f"{ent.nom} est en feu et subira {brulure_degats} dégâts pendant {brulure_duree} tours.")
        ent.statistiques['brulure_duree'] = brulure_duree
        ent.statistiques['brulure_degats'] = brulure_degats

class Feu(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_feu)

def utiliser_eau(sort, ent):
    """
    Cette fonction applique le sort d'eau sur une entité (ent).
    Elle inflige des dégâts initiaux et peut appliquer un effet de ralentissement.
    """
    degats_eau = sort['degats']  # Dégâts immédiats du sort d'eau
    reduction_force = sort.get('reduction_force', 0)  # Réduction de la force si le sort en a
    ralentissement_duree = sort.get('ralentissement_duree', 0)  # Durée de l'effet de ralentissement

    # Infliger les dégâts immédiats
    print(f"{sort['nom']} inflige {degats_eau} dégâts à {ent.nom}.")
    ent.statistiques['hp'] -= degats_eau

    # S'assurer que les HP ne tombent pas en dessous de 0
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher les PV après l'attaque initiale
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")

    # Appliquer l'effet de ralentissement (réduction de force) si disponible
    if ralentissement_duree > 0:
        print(f"{ent.nom} est ralenti et sa force est réduite de {reduction_force} pour {ralentissement_duree} tours.")
        ent.statistiques['force'] -= reduction_force
        # On peut stocker les effets temporaires dans des variables comme brulure_duree
        ent.statistiques['ralentissement_duree'] = ralentissement_duree
        ent.statistiques['reduction_force'] = reduction_force

class Eau(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_eau)

def utiliser_lumiere(sort, ent):
    """
    Applique le sort de lumière sur une entité (ent).
    Inflige des dégâts de lumière et peut soigner ou révéler des effets négatifs.
    """
    degats_lumiere = sort['degats']  # Dégâts infligés par la lumière
    soin_effet = sort.get('soin_effet', 0)  # Quantité de soin si c'est un effet positif
    purifie = sort.get('purifie', False)  # Vérifie si le sort retire des effets négatifs

    # Infliger les dégâts de lumière
    print(f"{sort['nom']} inflige {degats_lumiere} dégâts à {ent.nom}.")
    ent.statistiques['hp'] -= degats_lumiere

    # S'assurer que les HP ne tombent pas en dessous de 0
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher les PV après l'attaque
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")

    # Appliquer les soins si c'est une entité alliée
    if soin_effet > 0:
        ent.statistiques['hp'] += soin_effet
        if ent.statistiques['hp'] > ent.statistiques['hpmax']:
            ent.statistiques['hp'] = ent.statistiques['hpmax']
        print(f"{ent.nom} est soigné de {soin_effet} PV, et a maintenant {ent.statistiques['hp']} PV.")

    # Purifier les effets négatifs
    if purifie:
        if 'poison' in ent.statistiques:
            del ent.statistiques['poison']  # Retire l'effet de poison par exemple
            print(f"{ent.nom} est purifié de l'effet de poison.")
        else:
            print(f"{ent.nom} n'a aucun effet négatif à purifier.")

class Lumiere(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_lumiere)

def utiliser_vent(sort, ent):
    """
    Applique le sort de vent sur une entité (ent).
    Inflige des dégâts de vent et peut repousser ou réduire l'agilité de l'entité.
    """
    degats_vent = sort['degats']  # Dégâts infligés par le vent
    repousse = sort.get('repousse', False)  # Effet de repoussement
    reduction_agilite = sort.get('reduction_agilite', 0)  # Réduction de l'agilité

    # Infliger les dégâts de vent
    print(f"{sort['nom']} inflige {degats_vent} dégâts à {ent.nom}.")
    ent.statistiques['hp'] -= degats_vent

    # S'assurer que les HP ne tombent pas en dessous de 0
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher les PV après l'attaque
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")

    # Appliquer l'effet de repoussement
    if repousse:
        print(f"{ent.nom} est repoussé(e) par une bourrasque de vent.")

    # Réduire l'agilité de l'entité si applicable
    if reduction_agilite > 0:
        ent.statistiques['agilite'] = max(0, ent.statistiques.get('agilite', 0) - reduction_agilite)
        print(f"L'agilité de {ent.nom} est réduite de {reduction_agilite}. Agilité actuelle: {ent.statistiques['agilite']}.")


class Eau(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_vent)

def utiliser_tenebre(sort, ent):
    """
    Applique le sort de ténèbres sur une entité (ent).
    Inflige des dégâts d'ombre et peut affaiblir ou réduire la vision de l'entité.
    """
    degats_tenebre = sort['degats']  # Dégâts infligés par le sort de ténèbres
    affaiblissement_force = sort.get('affaiblissement_force', 0)  # Réduction de la force
    reduction_vision = sort.get('reduction_vision', False)  # Réduction de la vision de la cible

    # Infliger les dégâts de ténèbres
    print(f"{sort['nom']} inflige {degats_tenebre} dégâts de ténèbres à {ent.nom}.")
    ent.statistiques['hp'] -= degats_tenebre

    # S'assurer que les HP ne tombent pas en dessous de 0
    if ent.statistiques['hp'] < 0:
        ent.statistiques['hp'] = 0

    # Afficher les PV après l'attaque
    print(f"{ent.nom} a maintenant {ent.statistiques['hp']} PV.")

    # Affaiblir la force de l'entité
    if affaiblissement_force > 0:
        ent.statistiques['force'] = max(0, ent.statistiques.get('force', 0) - affaiblissement_force)
        print(f"La force de {ent.nom} est réduite de {affaiblissement_force}. Force actuelle: {ent.statistiques['force']}.")

    # Réduire la vision de l'entité si applicable
    if reduction_vision:
        print(f"{ent.nom} est enveloppé(e) dans les ténèbres, sa vision est réduite.")

class Tenebre(Sort):
    def __init__(self, nom: str, desc: str, mana: int, proprietes: dict):
        super().__init__(nom, desc, mana, proprietes, utiliser_tenebre)


