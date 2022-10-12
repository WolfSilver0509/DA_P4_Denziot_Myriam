from tinydb import TinyDB, Query 

from models.entities.Tournoi import Tournoi

class TournoisManager():
  """ Manager des tournois """
  def __init__(self): 
    self.db = TinyDB('db.json')
    self.table = self.db.table('tournois')

  def add(self, tournoi: Tournoi):
    print(tournoi.nom)
    """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views Tournois"""
    self.table.insert({'Nom': tournoi.nom,
                    'Lieu': tournoi.lieu,
                    'Date de debut': tournoi.date_de_debut,
                    'Nombre de tours': tournoi.nombre_de_tours,
                    'Tournees': tournoi.tournees,
                    'Joueur': tournoi.joueur,
                    'Controle du temps': tournoi.controle_du_temps,
                    'Description': tournoi.description})

  def list(self): 
    """ Récupérer tous les tournois """
    tournois = self.table.all()
    instanciated_tournaments = []
    for tournoi in tournois:
      instanciated_tournaments.append(Tournoi(tournoi["Nom"], tournoi["Lieu"], tournoi["Date de debut"], tournoi["Nombre de tours"],tournoi["Tournees"],tournoi["Joueur"],tournoi["Controle du temps"],tournoi["Description"]))

    #NE PAS OUBLIER 
    return instanciated_tournaments
   