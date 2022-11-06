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


  def update(self, tour, matchs):
    """ Update des match dans le tour dans tourmanager"""
    Tours = Query() 
    Tournois = Query()
    # print(self.table.search(Tours.Index== tour.index))
    # print(tour)
    # print(matchs)
    self.table.update({'matchs': matchs}, Tours.Index == tour.index)
    table_tournois = self.db.table('tournois')
    player_list = []
    for match in matchs:
      player_list.append(match['joueur1'])
      player_list.append(match['joueur2'])
    table_tournois.update({'Joueurs': player_list}, Tournois.Index == tour.index_tournois)
    
    