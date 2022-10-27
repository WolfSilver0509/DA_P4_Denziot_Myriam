import json
from pprint import pprint

class ViewTournois():
  """Affichage des tournois en views """

  @staticmethod # statique methode  pas besoin d'instancier la class ( quand la méthode na pas besoin de faire appel à des prop ou à des méthodes de la class )
  def add_tournament(players):
    selected_players = []
    selected_players_json = []
    nom = input("Nom :  ")
    lieu = input("Lieu :  ")
    date_de_debut = input("Date_de_debut :  ")
    nombre_de_tours = input("Nombre de tours :  ")
    tournees = input("Tournees :  ")
    print(" Merci de selec vos 8 joueurs ")
    chosen_id = []
    while len(selected_players) < 8:
      for index,playerChoice in enumerate(players) :
        if(index not in chosen_id):
          print(f"{index} : {playerChoice['prenom']} {playerChoice['nom_de_famille']} ")
      joueur = input("Joueur :  ")
      chosen_id.append(joueur)
      selected_players_json.append(json.dumps(players[int(joueur)]))
      selected_players.append(players[int(joueur)])
    controle_du_temps = input("Controle du temps :  ")
    description = input("Description  :  ")
    # revoir la boucle l'index se fait pas

    return nom, lieu, date_de_debut, nombre_de_tours, tournees,selected_players_json, controle_du_temps, description,  selected_players 

  @staticmethod
  def add_tournament_success():
    print(" Tournois ajouté !!")
   
  @staticmethod
  def list_tournois(tournois):
    """Listes des tournois"""
    for tournoi in tournois:
      print(tournoi.nom)
      
  @staticmethod
  def error_players8():
    print("Il vous faut minimum 8 Joueurs pour lancer un tournois !")

  @staticmethod
  def display_message_start_tour(no_tour):
    print("Le tour "+str(no_tour)+" commence !")


