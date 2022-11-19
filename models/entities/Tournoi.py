
class Tournoi():
    """Modèle représentant un tournoi."""
    def __init__(
            self,
            index,
            nom,
            lieu,
            date_de_debut,
            nombre_de_tours,
            tournees, joueurs,
            controle_du_temps,
            description,
            termine=0):
        """Initialise les détails relatifs au tournoi."""
        self.index = index
        self.nom = nom
        self.lieu = lieu
        self.date_de_debut = date_de_debut
        self.nombre_de_tours = nombre_de_tours
        self.tournees = tournees
        self.joueurs = joueurs
        self.controle_du_temps = controle_du_temps
        self.description = description
        self.termine = termine
