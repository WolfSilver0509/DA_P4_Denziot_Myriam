class Tournoi():
  """Modèle représentant un tournois."""
  def __init__(self,nom,lieu,date_de_debut,nombre_de_tours,tournees,joueur,controle_du_temps,description):
    """Initialise les détails relatifs au tournois."""
    self.nom = nom
    self.lieu = lieu
    self. date_de_debut = date_de_debut
    self.nombre_de_tours = nombre_de_tours # régler sur 4 par default
    self.tournees = tournees
    self.joueur = joueur
    self.controle_du_temps = controle_du_temps
    self.description = description




"""
●	nom
●	lieu :
●	date
○	Jusqu'à présent, tous nos tournois sont des événements d'un jour, mais nous pourrions en organiser de plusieurs jours à l'avenir, ce qui devrait donc permettre de varier les dates.
●	nombre de tours
○	Réglez la valeur par défaut sur 4.
●	Tournées
○	La liste des instances rondes.
●	joueurs
○	Liste des indices correspondant aux instances du joueur stockées en mémoire.
●	Contrôle du temps
○	C'est toujours un bullet, un blitz ou un coup rapide.
●	description
○	Les remarques générales du directeur du tournoi vont ici.

Objectifs premier tours - crée les joueurs - crée un tournois , ajouter les joueurs 
Premier tour - recup 
"""
