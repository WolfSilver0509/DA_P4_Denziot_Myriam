from tinydb import TinyDB, Query 
from models.entities.Tour import Tour

class TourManager():
  """ Manager de tour """
  def __init__(self): 
    self.db = TinyDB('db.json')
    self.table = self.db.table('tours')

  def add(self, tour: Tour):
    """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views"""
    self.table.insert({'nom': tour.nom,
                    'date_heure_debut': tour.date_heure_debut,
                    'date_heure_fin': tour.date_heure_fin})
