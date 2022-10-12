class ViewPlayer():
  """Affichage player en views """

  @staticmethod # statique methode  pas besoin d'instancier la class ( quand la méthode na pas besoin de faire appel à des prop ou à des méthodes de la class )
  def add_player():
    """ methode dans la views pour demander de rentrer les informations /"""

    nom_de_famille = input("Nom :  ")
    prenom = input("Prenom :  ")
    date_de_naissance = input("Date de naissance :  ")
    sexe = input("Sexe :  ")
    classement = input("Classement :  ")

    return nom_de_famille, prenom, date_de_naissance, sexe, classement

  @staticmethod
  def add_player_success():
    print(" Joueur ajouté !")
   
  @staticmethod
  def list_players(players):
    """Liste des joueurs"""
    for player in players:
      print(player.prenom)
    

   


