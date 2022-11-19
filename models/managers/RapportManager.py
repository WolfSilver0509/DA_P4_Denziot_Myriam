from tinydb import TinyDB, Query
from models.entities import Joueur


class RapportManager():
    """ rapport manager dans entitie manager """
    def __init__(self):
        self.db = TinyDB('db.json')
        self.table_tournament = self.db.table('tournois')
        self.table_tour = self.db.table('tours')

    def get_list_player_alpha(self,tournoi_choice):
        Tournois = Query()
        tournois = self.table_tournament.search(Tournois.Index == int(tournoi_choice))
        #print(tournois[0]['Joueurs'])
        players = tournois[0]['Joueurs']
        players = sorted(players, key=lambda x: x['nom_de_famille'], reverse=False)
        return players


    def get_list_player_ranking(self,tournoi_choice):
        Tournois = Query()
        tournois = self.table_tournament.search(Tournois.Index == int(tournoi_choice))
        players = tournois[0]['Joueurs']
        players = sorted(players, key=lambda x: x['classement'], reverse=False)
        return players

    def get_list_tour_in_tournament(self, tournoi_choice):
        Tour = Query()
        tour = self.table_tour.search(Tour.Index_tournois == int(tournoi_choice))
        return tour

    def get_list_match_in_tournament(self, tournoi_choice):
        Tour = Query()
        tour = self.table_tour.search(Tour.Index_tournois == int(tournoi_choice))
        return tour