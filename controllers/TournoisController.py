from pprint import pprint
import operator
import json
import datetime
from views.tournois.tournois import ViewTournois
from models.entities.Tournoi import Tournoi
from models.entities.Tour import Tour
from models.entities.Match import Match # New
from models.managers.TournoisManager import TournoisManager
from models.managers.PlayerManager import PlayerManager
from models.managers.TourManager import TourManager
from models.managers.MatchManager import MatchManager
from views.matchs import ViewMatchs


class TournoisController():
  """ Definition constructor player controller Tournois"""
  def __init__(self):
    """Définis son manager ' il va gerer tiny db'"""
    self.tournoi_manager = TournoisManager()
    self.playerManager = PlayerManager()
    self.tour_manager = TourManager()
    self.match_manager = MatchManager()

  def add_tournament(self):
    """ Ajout du tournois via le controller qui va faire la liaison entre le model et la view """
    if self.playerManager.has_enough_players():
      players=self.playerManager.list()

      nom, lieu, date_de_debut, nombre_de_tours, tournees,joueurs_json, controle_du_temps, description, joueurs = ViewTournois.add_tournament(players)
      tournoi = Tournoi(nom, lieu, date_de_debut, nombre_de_tours, tournees,joueurs_json, controle_du_temps, description)
      self.tournoi_manager.add(tournoi)
      ViewTournois.add_tournament_success()
      self.go_play_tour(joueurs)
    else :
     ViewTournois.error_players8()
    

  def list_tournois(self):
    """ Fonction qui liste les players depuis tiny db dans tournois controller"""
    tournois = self.tournoi_manager.list()
    ViewTournois.list_tournois(tournois)

  def go_play_tour(self, joueurs):
    """ Lancement du Tour 1 dans tournois controller """
    
    for i in range(4):
      ViewTournois.display_message_start_tour(i)
      # Create tour
      tour = Tour("Round "+str(i), json.dumps(datetime.datetime.now(), default=str), '')
      self.tour_manager.add(tour)
      joueurs = sorted(joueurs, key=lambda x: int(x['classement']), reverse= True )
      #pprint(joueurs) # trie des joueurs par classement 
      matchs = []
      mid_joueurs = 4
      for index in range(0, mid_joueurs):
        joueur1 = joueurs[index]
        joueur2 = joueurs[mid_joueurs+index]

        resultatJ1, resultatJ2 = ViewMatchs.indicate_results(joueur1, joueur2)
        match = Match(joueur1,joueur2, resultatJ1, resultatJ2)
        self.match_manager.add(match)
        
        matchs.append(match)

      pprint(matchs)
        
      exit()
      #Definir match
      
      
      
      
      
    