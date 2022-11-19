from tinydb import TinyDB
from models.entities.Match import Match


class MatchManager():
    """ Manager de match """
    def __init__(self):
        self.db = TinyDB('db.json')
        self.table = self.db.table('matchs')

    def add(self, match: Match):
        """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views"""
        self.table.insert(
            {'joueur1': match.joueur1,
             'joueur2': match.joueur2,
             'resultatJ1': match.resultatJ1,
             'resultatJ2': match.resultatJ2})
