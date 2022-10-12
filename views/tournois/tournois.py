class ViewTournois():
  """Affichage des tournois en views """

  @staticmethod # statique methode  pas besoin d'instancier la class ( quand la méthode na pas besoin de faire appel à des prop ou à des méthodes de la class )
  def add_tournament():
    nom = input("Nom :  "),
    lieu = input("Lieu :  "),
    date_de_debut = input("Date_de_debut :  "),
    nombre_de_tours = input("Nombre de tours :  "),
    tournees = input("Tournees :  "),
    joueur = input("Joueur :  "),
    controle_du_temps = input("Controle du temps :  "),
    description = input("Description  :  ")

    return nom, lieu, date_de_debut, nombre_de_tours, tournees,joueur, controle_du_temps, description   

  @staticmethod
  def add_tournament_success():
    print(" Tournois ajouté !!")
   
  @staticmethod
  def list_tournois(tournois):
    """Listes des tournois"""
    for tournoi in tournois:
      print(tournoi.nom)
     

   


