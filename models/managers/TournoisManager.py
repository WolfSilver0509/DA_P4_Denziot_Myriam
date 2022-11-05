from tinydb import TinyDB, Query 

from models.entities.Tournoi import Tournoi

class TournoisManager():
  """ Manager des tournois """
  def __init__(self): 
    self.db = TinyDB('db.json')
    self.table = self.db.table('tournois')

  def add(self, tournoi: Tournoi):
    #print(tournoi.nom)
    """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views Tournois"""
    self.table.insert({'Index': tournoi.index,
                    'Nom': tournoi.nom,
                    'Lieu': tournoi.lieu,
                    'Date de debut': tournoi.date_de_debut,
                    'Nombre de tours': tournoi.nombre_de_tours,
                    'Tournees': tournoi.tournees,
                    'Joueurs': tournoi.joueurs,
                    'Controle du temps': tournoi.controle_du_temps,
                    'Description': tournoi.description})

  def list(self): 
    """ Récupérer tous les tournois """
    tournois = self.table.all()
    instanciated_tournaments = []
    for tournoi in tournois:
      instanciated_tournaments.append(Tournoi(tournoi["Index"], tournoi["Nom"], tournoi["Lieu"], tournoi["Date de debut"], tournoi["Nombre de tours"],tournoi["Tournees"],tournoi["Joueurs"],tournoi["Controle du temps"],tournoi["Description"])) 
    return instanciated_tournaments

    
  def list_index(self): 
    """ Récupérer list index """
    tournois = self.table.all()
    if tournois : 
      index = tournois[-1]['Index']+1
    else:
      index=1
    return index

  def get_tournament_by_index(self, index): 
    """ Récupérer tournois par index dans tournois manager  """
    Tournoi = Query()
    tournois = self.table.search(Tournoi.Index == index)
    # Faire retourner le tournois en question 
    return tournois

  def recup_step_actualy(self, tournoi):
    """ Recupération etapes actuels dans tournois manager """
    table = self.db.table('tours')
    Tour = Query()
    print(tournoi)
    # doit afficher tournois en questions puis ligne 55 et 56 faire marcher
    # tour= table.search(Tour.Index_tournois == tournoi[0]['Index'])
    # print(tournoi[0]['Index'])
    #print(tour)
      
    
    