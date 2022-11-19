
class ViewTours():
    """Modèle représentant un tour dans la view tour."""

    @staticmethod
    def here_are_the_pairs():
        """ message d'affichage pour les paires dans View Tour"""
        print("Voici les paires de joueurs qui vont s'affronter : ")

    @staticmethod
    def display_joueurs_match(joueur1, joueur2):
        """ message d'affichage des joueurs contres joueurs """
        J1 = f"{joueur1['nom_de_famille']} {joueur1['prenom']}"
        J2 = f" {joueur2['nom_de_famille']} {joueur2['prenom']}"
        print(f"Le match va opposé {J1} contre {J2}")
        # print(f" {joueur1['nom_de_famille']} {joueur1['prenom']}
        # va affronter {joueur2['nom_de_famille']} {joueur2['prenom']} ")
