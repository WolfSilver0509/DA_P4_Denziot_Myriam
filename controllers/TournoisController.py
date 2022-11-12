from pprint import pprint
import operator
import json
import datetime
import random
from views.tournois import ViewTournois
from models.entities.Tournoi import Tournoi
from models.entities.Tour import Tour
from models.entities.Match import Match # New
from models.managers.TournoisManager import TournoisManager
from models.managers.PlayerManager import PlayerManager
from models.managers.TourManager import TourManager
from models.managers.MatchManager import MatchManager
from views.matchs import ViewMatchs
from views.tours import ViewTours

class TournoisController():
    """ Definition constructor player controller Tournois """
    def __init__(self):
        """Définis son manager ' il va gerer tiny db'"""
        self.tournoi_manager = TournoisManager()
        self.playerManager = PlayerManager()
        self.tour_manager = TourManager()
        self.match_manager = MatchManager()

    def add_tournament(self):
        """ Ajout du tournois via le controller qui va faire la liaison entre le model et la view """
        if self.playerManager.has_enough_players():
            index = self.tournoi_manager.list_index()
            players=self.playerManager.list()
            nom, lieu, date_de_debut, nombre_de_tours, tournees,joueurs_json, controle_du_temps, description, joueurs = ViewTournois.add_tournament(players)
            tournoi = Tournoi(index, nom, lieu, date_de_debut, nombre_de_tours, tournees,joueurs_json, controle_du_temps, description)
            self.tournoi_manager.add(tournoi)
            ViewTournois.add_tournament_success()
            self.question_tour_start_stop(joueurs, index)
            #self.go_play_tour(joueurs)
        else :
            ViewTournois.error_players8()

    def question_tour_start_stop(self,joueurs, index_tournois):
        """ Question avec condition : Si on commence un tour ou alors on quitte le programme dans controller tournois """
        question = ViewMatchs.question_start_stop()
        if question.startswith('o'):
            self.go_play_tour(joueurs, index_tournois)

    def list_tournois(self):
        """ Fonction qui liste les players depuis tiny db dans tournois controller"""
        tournois = self.tournoi_manager.list()
        ViewTournois.list_tournois(tournois)

    def back_up_tournament(self,):
        """ Fonction qui liste les tournois depuis tiny db dans tournois controller"""
        tournois = self.tournoi_manager.list()
        choice = ViewTournois.choice_tournament(tournois)
        tournoi = self.tournoi_manager.get_tournament_by_index(choice)
        tour_actualy = self.tournoi_manager.recup_step_actualy(tournoi)
        joueurs = tournoi[0]['Joueurs']
        index = tournoi[0]['Index']
        if tour_actualy == 0:
            print("lancer tour 1")
            self.question_tour_start_stop(joueurs, index)
        elif tour_actualy == 1:
            print("Lancer 2")
            self.go_play_tour_2(joueurs, index)
        elif tour_actualy == 2:
            print("Lancer 3")
        elif tour_actualy == 3:
            print("Lancer 4")
        elif tour_actualy == 4:
            print("Tournois finis")
        #print(tournoi)

    def go_play_tour(self, joueurs, index_tournois):
        """ Lancement du Tour 1 dans tournois controller """
        for i in range(4):
            ViewTournois.display_message_start_tour(i)
            # Create tour
            index_tour = self.tour_manager.list_index()
            tour = Tour(index_tour, index_tournois, "Round "+str(i), json.dumps(datetime.datetime.now(), default=str), '')
            self.tour_manager.add(tour)
            joueurs = sorted(joueurs, key=lambda x: int(x['classement']), reverse= True )
            #pprint(joueurs) # trie des joueurs par classement
            matchs = []
            ongoing_matchs = []
            mid_joueurs = 4

            ViewTours.here_are_the_pairs()
            for index in range(0, mid_joueurs):
                joueur1 = joueurs[index]
                joueur2 = joueurs[mid_joueurs+index]
                ongoing_matchs.append([joueur1, joueur2])
                ViewTours.display_joueurs_match(joueur1, joueur2)

            for paires in ongoing_matchs:
                joueur1 = paires[0]
                joueur2 = paires[1]
                k = random.randint(0, 1)
                if(k == 0):
                    couleur_joueur1 = 'Blanc'
                    couleur_joueur2 = 'Noir'
                else:
                    couleur_joueur1 = 'Noir'
                    couleur_joueur2 = 'Blanc'
                resultatJ1, resultatJ2 = ViewMatchs.indicate_results(joueur1, joueur2, couleur_joueur1, couleur_joueur2)
                joueur1['total_score'] += resultatJ1
                joueur2['total_score'] += resultatJ2
                match = Match(joueur1,joueur2, resultatJ1, resultatJ2)
                self.match_manager.add(match)
                matchs.append(match.serialize_match())
                tour.add_match(match)
            self.tour_manager.update(tour, matchs)
            #pprint(matchs)
            exit()
            #Definir match



    def go_play_tour_2(self, joueurs, index_tournois,n_tour):
        """lancer le tour 2 dans tournois controller """
        joueurs = sorted(joueurs, key=lambda x: float(x['total_score']), reverse= True )
        matchs = []
        match_current_tour = []
        index_tour = self.tour_manager.list_index()
        tour = Tour(index_tour, index_tournois, "Round " + str(n_tour), json.dumps(datetime.datetime.now(), default=str), '')
        #Rajouter n_tour a go play tour 2 quand je l'appelle . tour 2 = 1 etc
        self.tour_manager.add(tour)
        for i, joueur_1 in enumerate(joueurs):
            for joueur_2 in joueurs[1:]:
                match_exist = self.tour_manager.verif_joueur_play_back(joueur_1, joueur_2, index_tournois)
                current_match_exist = False
                if match_exist :
                    pass
                else:
                    if match_current_tour:
                        #print("existe")
                        current_match_exist = self.tour_manager.verif_joueur_play_current_tour(
                            joueur_1,
                            joueur_2,
                            match_current_tour
                        )
                    if not current_match_exist and joueur_1['nom_de_famille'] != joueur_2['nom_de_famille']:
                        print(joueur_1['nom_de_famille'], joueur_2['nom_de_famille'])
                        k = random.randint(0, 1)
                        if(k == 0):
                            couleur_joueur1 = 'Blanc'
                            couleur_joueur2 = 'Noir'
                        else:
                            couleur_joueur1 = 'Noir'
                            couleur_joueur2 = 'Blanc'
                        resultatJ1, resultatJ2 = ViewMatchs.indicate_results(joueur_1, joueur_2, couleur_joueur1, couleur_joueur2)
                        joueur_1['total_score'] += resultatJ1
                        joueur_2['total_score'] += resultatJ2
                        match = Match(joueur_1,joueur_2, resultatJ1, resultatJ2)
                        self.match_manager.add(match)
                        matchs.append(match.serialize_match())
                        match_current_tour.append(match.serialize_match())
                        tour.add_match(match)
        self.tour_manager.update(tour, matchs)
        print("Tour 2 Terminer")

        # autre veirifcation qui vérifie si le match qu'on veut crée n'existe pas dns le tour qu'on veut crée ( Match variable stockage de match avant de rentrer dans la boucle for init variable match lorsuq'on est dans le else on va verifier si ca verifie au match ( params joueur 1 joueur 2  match ))


      
    
        
    