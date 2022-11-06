from tinydb import TinyDB, Query 
from models.entities.Joueur import Joueur

class PlayerManager():
  """ Manager de player """
  def __init__(self): 
    self.db = TinyDB('db.json')
    self.table = self.db.table('joueurs')

  def add(self, player: Joueur):
    """ Taper dans tiny db pour inserer dans la table les donnés saisie dans player manager"""
    print(player.nom_de_famille)
    self.table.insert({'Nom': player.nom_de_famille,
                    'Prenom': player.prenom,
                    'Date_de_naissance': player.date_de_naissance,
                    'Sexe': player.sexe,
                    'Classement': player.classement,
                    'total_score' : player.total_score})

  def list(self): 
    """ Récupérer tous les players dans player manager """
    #names = [player.get('Nom') for player in self.table.all()]
     #= [player.get('Nom') for player in self.table.all()]
    players = self.table.all()
    instanciated_players = []
    for player in players:
      joueur= Joueur(player["Nom"], player["Prenom"], player["Date_de_naissance"], player["Sexe"], player["Classement"], player["total_score"]).serializer_player()
      instanciated_players.append(joueur)

    #NE PAS OUBLIER 
    return instanciated_players
    #print(names)  # List of all text field values.

  def has_enough_players(self):
    """ Fonction pour verifier les 8 joueurs dans player manager"""
    return len(self.table)>= 8