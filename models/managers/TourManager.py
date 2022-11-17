from tinydb import TinyDB, Query
from models.entities.Tour import Tour

class TourManager():
    """ Manager de tour """
    def __init__(self):
        self.db = TinyDB('db.json')
        self.table = self.db.table('tours')

    def add(self, tour: Tour):
        """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views"""
        self.table.insert({'Index': tour.index,
                           'Index_tournois': tour.index_tournois,
                           'nom': tour.nom,
                           'date_heure_debut': tour.date_heure_debut,
                           'date_heure_fin': tour.date_heure_fin,
                           'matchs': []})

    def list_index(self):
        """ Récupérer list index """
        tours = self.table.all()
        if tours :
            index = tours[-1]['Index']+1
        else:
            index=1

        #NE PAS OUBLIER
        return index


    def update(self, tour, matchs, joueurs):
        """ Update des match dans le tour dans tourmanager"""
        Tours = Query()
        Tournois = Query()
        player_not_play = []
        for joueur in joueurs:
            exist_player = [p for p in matchs if p['joueur1']['nom_de_famille'] == joueur['nom_de_famille'] or p['joueur2']['nom_de_famille'] == joueur['nom_de_famille']]

            if not exist_player:
                player_not_play.append(joueur)
        print(player_not_play)
        # print(self.table.search(Tours.Index== tour.index))
        # print(tour)
        # print(matchs)
        self.table.update({'matchs': matchs}, Tours.Index == tour.index)
        table_tournois = self.db.table('tournois')
        player_list = []
        for match in matchs:
            player_list.append(match['joueur1'])
            player_list.append(match['joueur2'])
        for player in player_not_play:
            player_list.append(player)
        table_tournois.update({'Joueurs': player_list}, Tournois.Index == tour.index_tournois)

    def recup_all_match_in_tour(self, index_tournois):
        """ Récupération de tous les tour via search dans tourManager"""
        Tours=Query()
        list_tour = self.table.search(Tours.Index_tournois == index_tournois)
        #rint(list_tour)
        match = []
        for tour in list_tour:
            match.extend(tour['matchs'])
        return match

    def verif_joueur_play_back(self, joueur_1, joueur_2, index ):
        """ Verification si le joueur à deja jouer dans un match dans tourmanager"""
        old_match = self.recup_all_match_in_tour(index)
        #print(old_match)
        for match in old_match:
            # print(joueur_1['nom_de_famille'],joueur_2['nom_de_famille'] )
            # print(match['joueur1']['nom_de_famille'], " contre ", match['joueur2']['nom_de_famille'])
            #print("="*100)
            OJ1 = match['joueur1']['nom_de_famille']
            OJ2 = match['joueur2']['nom_de_famille']
            J1 = joueur_1['nom_de_famille']
            J2 = joueur_2['nom_de_famille']
            if (J1 == OJ1 and J2 == OJ2) or (J1 == OJ2 and J2 == OJ1):
                return True
        return False
#Commentaires
    def verif_joueur_play_current_tour(self, joueur_1, joueur_2, match_current_tour ):
        """ Verification si le joueur à deja jouer dans le match actuel dans tourmanager"""
        old_match = match_current_tour
        #print(old_match)
        for match in old_match:
            # print(joueur_1['nom_de_famille'],joueur_2['nom_de_famille'] )
            # print(match['joueur1']['nom_de_famille'], " contre ", match['joueur2']['nom_de_famille'])
            #print("="*100)
            OJ1 = match['joueur1']['nom_de_famille']
            OJ2 = match['joueur2']['nom_de_famille']
            J1 = joueur_1['nom_de_famille']
            J2 = joueur_2['nom_de_famille']
            if (J1 == OJ1 and J2 == OJ2) or (J1 == OJ2 and J2 == OJ1) or (J1 == OJ1 or J1 == OJ2) or (J2 == OJ1 or J2 == OJ2):
                return True
        return False
      
    def recup_all_match(self):
        """ Récupération de tous les tour via search dans tourManager"""
        Tours = Query()
        list_match = self.db.table('matchs').all()
        #rint(list_tour)

        return list_match
    
