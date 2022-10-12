from views.tournois.tournois import ViewTournois
from models.entities.Tournoi import Tournoi
from models.managers.TournoisManager import TournoisManager

class TournoisController():
  """ Definition constructor player controller Tournois"""
  def __init__(self):
    """Définis son manager ' il va gerer tiny db'"""
    self.tournoi_manager = TournoisManager()

  def add_tournament(self):
    """ Ajout du tournois via le controller qui va faire la liaison entre le model et la view """
   
    nom, lieu, date_de_debut, nombre_de_tours, tournees,joueur, controle_du_temps, description = ViewTournois.add_tournament()
    tournoi = Tournoi(nom, lieu, date_de_debut, nombre_de_tours, tournees,joueur, controle_du_temps, description)
    self.tournoi_manager.add(tournoi)
    ViewTournois.add_tournament_success()

  def list_tournois(self):
    """ Fonction qui liste les players depuis tiny db"""
    tournois = self.tournoi_manager.list()
    ViewTournois.list_tournois(tournois)
