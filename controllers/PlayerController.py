from views.player import ViewPlayer
from models.entities.Joueur import Joueur
from models.managers.PlayerManager import PlayerManager


class PlayerController:
    """Definition constructor player controller"""

    def __init__(self):
        """Définis son manager ' il va gerer tiny db'"""
        self.player_manager = PlayerManager()

    def add_player(self):
        """Instancier l'entité l15 / l16 j'appel mon manager dans laquel metho add dans player controller"""
        index = self.player_manager.list_index()
        (
            nom_de_famille,
            prenom,
            date_de_naissance,
            sexe,
            classement,
            total_score,
        ) = ViewPlayer.add_player()
        player = Joueur(
            index, nom_de_famille, prenom, date_de_naissance, sexe, classement, total_score
        )
        self.player_manager.add(player)
        ViewPlayer.add_player_success()

    def list_players(self):
        """Fonction qui liste les players depuis tiny db dans player controller"""
        players = self.player_manager.list()
        ViewPlayer.list_players(players)

    def list_players_by_rank(self):
        """Fonction qui liste les players par rank depuis tiny db dans player controller"""
        players = self.player_manager.list_by_rank()
        ViewPlayer.list_players(players)

    def update_rank(self):
        """Fonction qui update le rank depuis tiny db dans player controller"""
        players = self.player_manager.list_by_rank()
        player, classement = ViewPlayer.update_rank(players)
        self.player_manager.update_player_rank(player, classement)
