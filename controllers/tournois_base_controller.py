from models.managers.TournoisManager import TournoisManager
from models.managers.PlayerManager import PlayerManager
from models.managers.TourManager import TourManager
from models.managers.MatchManager import MatchManager
from views.menu_rapport import ViewRapport
from models.managers.RapportManager import RapportManager
from views.player import ViewPlayer
class BaseTournoisController():
    """ Base controller a mettre dans tournois controller pour ne pas ralentir le programme """

    def __init__(self):
        """Définis son manager ' il va gerer tiny db'"""
        self.tournoi_manager = TournoisManager()
        self.playerManager = PlayerManager()
        self.tour_manager = TourManager()
        self.match_manager = MatchManager()
        self.rapport_manager = RapportManager()


    def recup_choice_to_play(self,tournoi_choice):
        """ fonction pour recupérer le choix de l'utilisateur"""
        choice = ViewRapport().menu_option_tournoi()
        if choice == 1:
            self.list_player_tournament_alpha(tournoi_choice)
        elif choice == 2:
            self.list_player_tournament_ranking(tournoi_choice)
        elif choice == 3:
            self.list_tour_in_tournament(tournoi_choice)
        elif choice == 4:
            self.list_match_in_tournament(tournoi_choice)
        elif choice == 5:
            print("Retour au menu tournois")
        if choice != 5:
            return self.recup_choice_to_play(tournoi_choice)

    def list_player_tournament_alpha(self, tournoi_choice):
        """ fonction pour la liste des joueurs par ordre alphabetique"""
        print("Liste des joueurs par ordre alphabetique : ")
        list_player = self.rapport_manager.get_list_player_alpha(tournoi_choice)
        ViewPlayer.list_players(list_player)

    def list_player_tournament_ranking(self, tournoi_choice):
        """ fonction pour la liste des joueurs par classement"""
        print("Liste des joueurs par classement :")
        list_player = self.rapport_manager.get_list_player_ranking(tournoi_choice)
        ViewPlayer.list_players(list_player)


    def list_tour_in_tournament(self, tournoi_choice):
        """ fonction pour la liste des tours dans un tournois"""
        print("Liste des tours dans un tournois")
        list_tour = self.rapport_manager.get_list_tour_in_tournament(tournoi_choice)
        ViewRapport().display(list_tour,1)


    def list_match_in_tournament(self, tournoi_choice):
        """ fonction pour la liste des matchs dans un tournois"""
        print("Liste des matchs dans un tournois")
        list_tour = self.rapport_manager.get_list_match_in_tournament(tournoi_choice)
        ViewRapport().display(list_tour, 0)
