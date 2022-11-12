

class Tour():
    """Modèle représentant un tour."""
    def __init__(self, index,index_tournois, nom, date_heure_debut, date_heure_fin):
        """Initialise les détails relatifs au tour."""
        self.index = index
        self.index_tournois = index_tournois
        self.nom = nom
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.matchs = []
        #ajout identifiant tournois auquels ils appartiens

    def add_match(self, match):
        """ Ajouter un match dans tour entities """
        self.matchs.append(match.serialize_match())

    def serialize_matchs(self):
        """ Fonction de serialisation de match dans tour entities modeles"""
        return self.matchs.__dict__

    def serialize_tour(self):
        return self.__dict__