from tinydb import TinyDB, Query 
from models.entities.Joueur import Joueur

class PlayerManager():
  """ Manager de player """
  def __init__(self): 
    self.db = TinyDB('db.json')
    self.table = self.db.table('joueurs')

  def add(self, player: Joueur):
    print(player.nom_de_famille)
    """ Taper dans tiny db pour inserer dans la table les donnés saisie dans views"""
    self.table.insert({'Nom': player.nom_de_famille,
                    'Prenom': player.prenom,
                    'Date de naissance': player.date_de_naissance,
                    'Sexe': player.sexe,
                    'Classement': player.classement})

  def list(self): 
    """ Récupérer tous les players """
    #names = [player.get('Nom') for player in self.table.all()]
     #= [player.get('Nom') for player in self.table.all()]
    players = self.table.all()
    instanciated_players = []
    for player in players:
      instanciated_players.append(Joueur(player["Nom"], player["Prenom"], player["Date de naissance"], player["Sexe"], player["Classement"]))

    #NE PAS OUBLIER 
    return instanciated_players
    #print(names)  # List of all text field values.