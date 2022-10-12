class Tour():
  """Modèle représentant un tour."""
  def __init__(self, nom, date_heure_debut, date_heure_fin):
    """Initialise les détails relatifs au tour."""
    self.nom = nom
    self.date_heure_debut = date_heure_debut
    self.date_heure_fin = date_heure_fin