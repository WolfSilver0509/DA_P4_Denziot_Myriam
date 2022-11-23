from tinydb import TinyDB, Query
from models.entities.Joueur import Joueur


class PlayerManager:
    """Manager de player"""

    def __init__(self):
        self.db = TinyDB("db.json")
        self.table = self.db.table("joueurs")

    def add(self, player: Joueur):
        """Taper dans tiny db pour insérer dans la table les données saisies dans player manager"""
        print(player.nom_de_famille)
        self.table.insert(
            {
                "Index": player.index,
                "Nom": player.nom_de_famille,
                "Prenom": player.prenom,
                "Date_de_naissance": player.date_de_naissance,
                "Sexe": player.sexe,
                "Classement": player.classement,
                "total_score": player.total_score,
            }
        )

    def list(self):
        """Récupérer tous les players dans player manager"""
        players = self.table.all()
        players = sorted(players, key=lambda x: x["Nom"], reverse=False)
        instanciated_players = []
        for player in players:
            joueur = Joueur(
                player["Index"],
                player["Nom"],
                player["Prenom"],
                player["Date_de_naissance"],
                player["Sexe"],
                player["Classement"],
                player["total_score"],
            ).serializer_player()
            instanciated_players.append(joueur)
        return instanciated_players

    def has_enough_players(self):
        """Fonction pour verifier les 8 joueurs dans player manager"""
        return len(self.table) >= 8

    def list_by_rank(self):
        """Récupérer tous les players par classement dans player manager"""
        players = self.table.all()
        players = sorted(players, key=lambda x: int(x["Classement"]))
        instanciated_players = []
        for player in players:
            joueur = Joueur(
                player["Index"],
                player["Nom"],
                player["Prenom"],
                player["Date_de_naissance"],
                player["Sexe"],
                player["Classement"],
                player["total_score"],
            ).serializer_player()
            instanciated_players.append(joueur)
        return instanciated_players

    def list_index(self):
        """Récupérer list index player manager"""
        joueurs = self.table.all()
        index = 1
        if joueurs:
            index = joueurs[-1]["Index"] + 1
        return index

    def update_player_rank(self, player, classement):
        """Fonction qui update le rank depuis tiny db dans player controller"""
        Player = Query()
        self.table.update({"Classement": classement}, Player.Index == int(player))
        # Update
        # 1 arguments disctionnaires de ce qui va changer
        # 2eme argument la condition de la requete
        # la condition se fait avec un Query qui vise la table
        # et la condition est le nom de la colonne et la valeur de la colonne
