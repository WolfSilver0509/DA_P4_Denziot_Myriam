import json

class Joueur():
  """Modèle représentant un joueur."""
  def __init__(self,nom_de_famille,prenom,date_de_naissance,sexe,classement, total_score):
    """Initialise les détails relatifs au joueur dans entities joueurs """
    self.nom_de_famille = nom_de_famille
    self.prenom = prenom
    self.date_de_naissance = date_de_naissance
    self.sexe = sexe
    self.classement = classement
    self.total_score = total_score

  def serializer_player (self):
    """ Fonction pour sérialiser notre objet joueur dans joueur entities ( prendre la class pour mettre sous forme de dictionnaire ) """
    return self.__dict__

   

# définis les attributs de la classe !
