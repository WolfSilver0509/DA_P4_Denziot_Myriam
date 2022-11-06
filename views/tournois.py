import json
from pprint import pprint
import uuid 
class ViewTournois():
  """Affichage des tournois en views """

  @staticmethod # statique methode  pas besoin d'instancier la class ( quand la méthode na pas besoin de faire appel à des prop ou à des méthodes de la class )
  def add_tournament(players):
    """ Ajouter un tournois dans views tournois"""
    selected_players = []
    selected_players_json = []
    nom = input("Nom :  ")
    lieu = input("Lieu :  ")
    date_de_debut = input("Date_de_debut :  ")
    nombre_de_tours = int(input("Nombre de tours (par défaut 4) : ") or "4")
    tournees = input("Tournees :  ")
    print(" Merci de selectionner 8 joueurs parmis les choix proposés, afin de pouvoir commencer un tournoi ! ")
    player_memory  = players
    chosen_id = []
    while len(selected_players) < 8:
      for index,playerChoice in enumerate(players) :
        print(f"{index} : {playerChoice['prenom']} {playerChoice['nom_de_famille']} ")
      joueur = input("Joueur :  ")
      chosen_id.append(joueur)
      selected_players_json.append(players[int(joueur)])
      selected_players.append(players[int(joueur)])
      players.pop(int(joueur))
    controle_du_temps = input("Controle du temps :  ")
    description = input("Description  :  ")
    players = player_memory
    # revoir la boucle l'index se fait pas

    return nom, lieu, date_de_debut, nombre_de_tours, tournees,selected_players_json, controle_du_temps, description,  selected_players 

  @staticmethod
  def add_tournament_success():
    """ message d'ajout de tournois avec succés dans views tournois"""
    print(" Le Tournoi a été ajouté avec succès ! ")
   
  @staticmethod
  def list_tournois(tournois):
    """Listes des tournois dans views tounois"""
    for tournoi in tournois:
      print(tournoi.nom)
     
      
  @staticmethod
  def error_players8():
     """ message d'erreur de tournois dans views tournois"""
     print("Il vous faut minimum 8 Joueurs pour lancer un tournois !")

  @staticmethod
  def display_message_start_tour(no_tour):
    """ message start tour views tournois"""
    print("Le tour "+str(no_tour)+" commence !")

  @staticmethod
  def choice_tournament(tournois):
    """Listes des choix tournois dans views tounois"""
    for tournoi in tournois:
      print(tournoi.index, tournoi.nom)
    choice = input("Choix du tournoi :  ")
    return choice

    
  


      

    

 
