from models.entities.Joueur import Joueur
# from TinyDB import joueur
from tinydb import TinyDB, Query 

db = TinyDB('db.json')
joueurs = db.table('joueurs')


class View(Joueur):
  
  
  def __init__(self,nom_de_famille,prenom,date_de_naissance,sexe,classement):
    super().__init__(nom_de_famille,prenom,date_de_naissance,sexe,classement)


  # def save_player_db(self):
  #   joueurs.insert({'nom': self.nom_de_famille})
  
  def add_player(self):

    nom_de_famille = input("Nom :  "),
    prenom = input("Prenom :  "),
    date_de_naissance = input("Date de naissance :  "),
    sexe = input("Sexe :  "),
    classement = input("Classement :  ")
    print(" Joueur ajouté !")
    joueurs.insert({'Nom': nom_de_famille,
                    'Prenom': prenom,
                    'Date de naissance': date_de_naissance,
                    'Sexe': sexe,
                    'Classement': classement})
    
  def list_of_player():
    pass
     # print(db.get(where('ID') == 1)
   


