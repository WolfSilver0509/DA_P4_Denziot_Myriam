from tinydb import TinyDB, Query

from models.entities.Tournoi import Tournoi


class TournoisManager:
    """Manager des tournois"""

    def __init__(self):
        self.db = TinyDB("db.json")
        self.table = self.db.table("tournois")

    def add(self, tournoi: Tournoi):
        """Taper dans tiny db pour insérer dans la table les données saisies dans views Tournois"""
        self.table.insert(
            {
                "Index": tournoi.index,
                "Nom": tournoi.nom,
                "Lieu": tournoi.lieu,
                "Date de debut": tournoi.date_de_debut,
                "Nombre de tours": tournoi.nombre_de_tours,
                "Tournees": tournoi.tournees,
                "Joueurs": tournoi.joueurs,
                "Controle du temps": tournoi.controle_du_temps,
                "Description": tournoi.description,
                "Termine": 0,
            }
        )

    def list(self):
        """Récupérer tous les tournois"""
        tournois = self.table.all()
        instanciated_tournaments = []
        for tournoi in tournois:
            instanciated_tournaments.append(
                Tournoi(
                    tournoi["Index"],
                    tournoi["Nom"],
                    tournoi["Lieu"],
                    tournoi["Date de debut"],
                    tournoi["Nombre de tours"],
                    tournoi["Tournees"],
                    tournoi["Joueurs"],
                    tournoi["Controle du temps"],
                    tournoi["Description"],
                )
            )
        return instanciated_tournaments

    def list_termine(self):
        """Récupérer tous les tournois non terminer"""
        Tournois = Query()
        tournois = self.table.search(Tournois.Termine == 0)
        instanciated_tournaments = []
        for tournoi in tournois:
            instanciated_tournaments.append(
                Tournoi(
                    tournoi["Index"],
                    tournoi["Nom"],
                    tournoi["Lieu"],
                    tournoi["Date de debut"],
                    tournoi["Nombre de tours"],
                    tournoi["Tournees"],
                    tournoi["Joueurs"],
                    tournoi["Controle du temps"],
                    tournoi["Description"],
                )
            )
        return instanciated_tournaments

    def list_index(self):
        """Récupérer list index"""
        tournois = self.table.all()
        if tournois:
            index = tournois[-1]["Index"] + 1
        else:
            index = 1
        return index

    def get_tournament_by_index(self, index):
        """Récupérer tournois par index dans tournois manager"""
        Tournoi = Query()
        tournois = self.table.search(Tournoi.Index == int(index))
        return tournois

    def recup_step_actualy(self, tournoi):
        """Recupération etapes actuels dans tournois manager"""
        table = self.db.table("tours")
        Tour = Query()
        tour = table.search(Tour.Index_tournois == tournoi[0]["Index"])
        if tour:
            if len(tour) >= 4:
                tour_actualy = 4
            elif len(tour) == 3:
                tour_actualy = 3
            elif len(tour) == 2:
                tour_actualy = 2
            elif len(tour) == 1:
                tour_actualy = 1
        else:
            tour_actualy = 0
        return tour_actualy

    def statut_tournois(self, index_tournois):
        """Statut tournois dans tournois manager"""
        Tournoi = Query()
        self.table.update({"Termine": 1}, Tournoi.Index == int(index_tournois))
