class ViewRapport:
    """Menu Rapport dans view menu repport"""

    def menu_option_tournoi(self):
        """Menu Option tournoi dans viewRapport"""
        menu_options_par_tournois = {
            1: "➕♟Listes joueurs par tournois par ordre alphabétique ♟ ♟",
            2: "📋♟Listes joueurs par tournois par classement ♟ ♟",
            3: "📋 Listes de tous les tour par tournois",
            4: "♟ Listes de tous les matchs par tournois",
            5: "♟ Modifier le classement d'un joueur",
            6: "Retour au menu",
        }

        for key in menu_options_par_tournois.keys():
            print(key, "--", menu_options_par_tournois[key])
        option = int(input("Entrer votre choix : "))
        return option

    def display(self, list_tour, step):
        """Affiche les tours d'un tournoi dans viewRapport"""
        for tour in list_tour:
            if step == 1:
                print(tour["nom"])
            for match in tour["matchs"]:
                print(
                    match["joueur1"]["nom_de_famille"],
                    match["resultatJ1"],
                    "vs",
                    match["joueur2"]["nom_de_famille"],
                    match["resultatJ2"],
                )

    def update_rank(self, players):
        """Méthode pour mettre à jour le classement des joueurs dans la views menu-rapport"""
        for player in players:
            print(
                str(
                    player["index"]
                ) + " " + player["prenom"] + " " + player["nom_de_famille"] + " " + player["classement"]
            )
        player = input("Joueur :  ")
        classement = input(" Nouveau Classement :  ")
        return player, classement
