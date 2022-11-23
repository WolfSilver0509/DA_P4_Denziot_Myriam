import json
import datetime
import random
from views.tournois import ViewTournois
from models.entities.Tournoi import Tournoi
from models.entities.Tour import Tour
from models.entities.Match import Match
from controllers.tournois_base_controller import BaseTournoisController
from views.matchs import ViewMatchs
from views.tours import ViewTours


class TournoisController(BaseTournoisController):
    """Definition constructor player controller Tournois"""

    def add_tournament(self):
        """Ajout du tournoi via le controller qui va faire la liaison entre le model et la view"""
        if self.playerManager.has_enough_players():
            index = self.tournoi_manager.list_index()
            players = self.playerManager.list()
            n, l, d, t, tour, jjs, cdt, desc, jou = ViewTournois.add_tournament(players)
            nom = n
            lieu = l
            date_de_debut = d
            nombre_de_tours = t
            tournees = tour
            joueurs_json = jjs
            controle_du_temps = cdt
            description = desc
            joueurs = jou
            tournoi = Tournoi(
                index,
                nom,
                lieu,
                date_de_debut,
                nombre_de_tours,
                tournees,
                joueurs_json,
                controle_du_temps,
                description,
            )
            self.tournoi_manager.add(tournoi)
            ViewTournois.add_tournament_success()
            self.question_tour_start_stop(joueurs, index, 1)
        else:
            ViewTournois.error_players8()

    def question_tour_start_stop(self, joueurs, index_tournois, n_tour_actualy):
        """Question avec condition : Reprendre ou quitter le tournois"""
        question = ViewMatchs.question_start_stop(n_tour_actualy)
        if question.startswith("o"):
            if n_tour_actualy == 1:
                self.go_play_tour(joueurs, index_tournois)
            elif n_tour_actualy == 2:
                self.go_play_tour_2(joueurs, index_tournois, 2)
            elif n_tour_actualy == 3:
                self.go_play_tour_2(joueurs, index_tournois, 3)
            elif n_tour_actualy == 4:
                self.go_play_tour_2(joueurs, index_tournois, 4)

    def list_tournois(self):
        """Fonction qui liste les players depuis tiny db dans tournois controller"""
        tournois = self.tournoi_manager.list()
        if tournois:
            choice = ViewTournois.choice_tournament(tournois)
            print(choice)
            tournoi_choice = self.tournoi_manager.get_tournament_by_index(choice)
            print(tournoi_choice)
            print("Tournois 1")
            self.recup_choice_to_play(choice)
        else:
            print("Pas de tournois en mémoire")

    def back_up_tournament(
        self,
    ):
        """Fonction qui liste les tournois depuis tiny db dans tournois controller"""
        tournois = self.tournoi_manager.list_termine()
        if tournois:
            choice = ViewTournois.choice_tournament(tournois)
            tournoi = self.tournoi_manager.get_tournament_by_index(choice)
            tour_actualy = self.tournoi_manager.recup_step_actualy(tournoi)
            joueurs = tournoi[0]["Joueurs"]
            index = tournoi[0]["Index"]
            if tour_actualy == 0:
                print("lancer tour 1")
                self.question_tour_start_stop(joueurs, index, 1)
            elif tour_actualy == 1:
                print("Lancer 2")
                self.question_tour_start_stop(joueurs, index, 2)
            elif tour_actualy == 2:
                print("Lancer 3")
                self.question_tour_start_stop(joueurs, index, 3)
            elif tour_actualy == 3:
                print("Lancer 4")
                self.question_tour_start_stop(joueurs, index, 4)
            elif tour_actualy == 4:
                print("Tournois finis")
                self.tournoi_manager.statut_tournois(index)
                match = self.tour_manager.recup_all_match()
                for nom in match:
                    print(
                        nom["joueur1"]["nom_de_famille"],
                        nom["joueur2"]["nom_de_famille"],
                    )
        else:
            print(" Tous les tournois sont terminés")

    def go_play_tour(self, joueurs, index_tournois):
        """Lancement du Tour 1 dans tournois controller"""

        ViewTournois.display_message_start_tour(1)
        # Create tour
        index_tour = self.tour_manager.list_index()
        tour = Tour(
            index_tour,
            index_tournois,
            "Round " + str(1),
            json.dumps(datetime.datetime.now(), default=str),
            "",
        )
        self.tour_manager.add(tour)
        joueurs = sorted(joueurs, key=lambda x: int(x["classement"]), reverse=True)
        matchs = []
        ongoing_matchs = []
        mid_joueurs = 4

        ViewTours.here_are_the_pairs()
        for index in range(0, mid_joueurs):
            joueur1 = joueurs[index]
            joueur2 = joueurs[mid_joueurs + index]
            ongoing_matchs.append([joueur1, joueur2])
            ViewTours.display_joueurs_match(joueur1, joueur2)

        for paires in ongoing_matchs:
            joueur1 = paires[0]
            joueur2 = paires[1]
            k = random.randint(0, 1)
            if k == 0:
                couleur_joueur1 = "Blanc"
                couleur_joueur2 = "Noir"
            else:
                couleur_joueur1 = "Noir"
                couleur_joueur2 = "Blanc"
            resultatJ1, resultatJ2 = ViewMatchs.indicate_results(
                joueur1, joueur2, couleur_joueur1, couleur_joueur2
            )
            joueur1["total_score"] += resultatJ1
            joueur2["total_score"] += resultatJ2
            match = Match(joueur1, joueur2, resultatJ1, resultatJ2)
            self.match_manager.add(match)
            matchs.append(match.serialize_match())
            tour.add_match(match)
        self.tour_manager.update(tour, matchs, joueurs)
        self.question_tour_start_stop(joueurs, index_tournois, 2)

    def go_play_tour_2(self, joueurs, index_tournois, n_tour):
        """Lancer le tour 2 dans tournois controller"""
        joueurs = sorted(joueurs, key=lambda x: float(x["total_score"]), reverse=True)
        matchs = []
        match_current_tour = []
        index_tour = self.tour_manager.list_index()
        time_now = json.dumps(datetime.datetime.now(), default=str)
        tour = Tour(index_tour, index_tournois, "Round " + str(n_tour), time_now, "")
        self.tour_manager.add(tour)
        for i, joueur_1 in enumerate(joueurs):
            for joueur_2 in joueurs:
                match_exist = self.tour_manager.verif_joueur_play_back(
                    joueur_1, joueur_2, index_tournois
                )
                current_match_exist = False
                if match_exist:
                    pass
                else:
                    if match_current_tour:
                        current_match_exist = (
                            self.tour_manager.verif_joueur_play_current_tour(
                                joueur_1, joueur_2, match_current_tour
                            )
                        )
                    if (
                        not current_match_exist and joueur_1["nom_de_famille"] != joueur_2["nom_de_famille"]
                    ):
                        print(joueur_1["nom_de_famille"], joueur_2["nom_de_famille"])
                        k = random.randint(0, 1)
                        if k == 0:
                            couleur_joueur1 = "Blanc"
                            couleur_joueur2 = "Noir"
                        else:
                            couleur_joueur1 = "Noir"
                            couleur_joueur2 = "Blanc"
                        resultatJ1, resultatJ2 = ViewMatchs.indicate_results(
                            joueur_1, joueur_2, couleur_joueur1, couleur_joueur2
                        )
                        joueur_1["total_score"] += resultatJ1
                        joueur_2["total_score"] += resultatJ2
                        match = Match(joueur_1, joueur_2, resultatJ1, resultatJ2)
                        self.match_manager.add(match)
                        matchs.append(match.serialize_match())
                        match_current_tour.append(match.serialize_match())
                        tour.add_match(match)
        self.tour_manager.update(tour, matchs, joueurs)
        if n_tour != 4:
            self.question_tour_start_stop(joueurs, index_tournois, n_tour + 1)
        else:
            print("Le tournois est terminé ! ")
            self.tournoi_manager.statut_tournois(index_tournois)
