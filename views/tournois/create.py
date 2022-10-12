from models.entities import Tournois
from tinydb import TinyDB, Query 

dbTournois = TinyDB('dbTournois.json')
tournois = dbTournois.table('tournois')


class View(Tournois):
  
  
   def __init__(self,nom,lieu,date,nombre_de_tours,tournees,joueur,controle_du_temps,description):
    super().__init__(self,nom,lieu,date,nombre_de_tours,tournees,joueur,controle_du_temps,description)


  # def save_player_db(self):
  #   joueurs.insert({'nom': self.nom})
  
 
    
    tournois.insert({'Nom': nom,
                    'Lieu': prenom,
                    'Date ': date,
                    'Nombre de tours': nombre_de_tours,
                     'Tournees': tournees,
                     'Joueur': joueur,
                     'Controle du temps': controle_du_temps,
                    'Description': description})
    
 
   