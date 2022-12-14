class ViewPlayer:
    """Affichage player en views"""

    @staticmethod
    # statique methode pas besoin d'instancier la class
    # ( quand la méthode n'a pas besoin de faire appel à des prop ou à des méthodes de la class )
    def add_player():
        """méthode dans la views pour demander de rentrer les informations /"""
        nom_de_famille = input("Nom :  ")
        prenom = input("Prenom :  ")
        date_de_naissance = input("Date de naissance :  ")
        sexe = input("Sexe :  ")
        classement = input("Classement :  ")
        total_score = 0

        return nom_de_famille, prenom, date_de_naissance, sexe, classement, total_score

    @staticmethod
    def add_player_success():
        """Fonction de print joueur ajouter avec succés Views players"""
        print(" Joueur ajouté !")

    @staticmethod
    def list_players(players):
        """Liste des joueurs dans la views player"""
        for player in players:
            print(
                player["classement"] + " " + player["nom_de_famille"] + " " + player["prenom"]
            )

    @staticmethod
    def update_rank(players):
        """Méthode pour mettre à jour le classement des joueurs dans la views player"""
        for player in players:
            print(
                str(
                    player["index"]
                ) + " " + player["prenom"] + " " + player["nom_de_famille"] + " " + player["classement"]
            )
        player = input("Joueur :  ")
        classement = input(" Nouveau Classement :  ")
        return player, classement
