from tinydb import TinyDB, Query



class RapportManager():
    """ rapport manager dans entitie manager """
    def __init__(self):
        self.db = TinyDB('db.json')
        self.table_tournament = self.db.table('tournois')
        self.table_tour = self.db.table('tours')

    def get_list_player_alpha(self,tournoi_choice):
        Tournois = Query()
        tournois = self.table_tournament.search(Tournois.Index == int(tournoi_choice))
        print(tournois)


    def get_list_player_ranking(self,tournoi_choice):
        pass

    def get_list_tour_in_tournament(self,tournoi_choice):
        pass

    def get_list_match_in_tournament(self,tournoi_choice):
        pass