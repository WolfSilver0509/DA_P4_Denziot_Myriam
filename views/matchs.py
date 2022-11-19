

class ViewMatchs():
    """Affichage Matchs en view"""

    @staticmethod
    def indicate_results(joueur1, joueur2, couleur_joueur1, couleur_joueur2):
        """ Affichage des résultats  dans views match """
        J1 = f" {joueur1['prenom']}  {joueur1['nom_de_famille']} (couleur jouée : {couleur_joueur1})"
        J2 = f" {joueur2['prenom']} {joueur2['nom_de_famille']} (couleur jouée : {couleur_joueur2})"
        print(f"Rentrez les résultats du match entre {J1} et {J2}")
        # print(f" Rentrez les résultats du match entre
        # {joueur1['prenom']}  {joueur1['nom_de_famille']} (couleur jouée : {couleur_joueur1}) et {joueur2['prenom']}
        # {joueur2['nom_de_famille']} (couleur jouée : {couleur_joueur2}): ")
        resultatJ1 = input('Résultat de '+joueur1['prenom']+' '+joueur1['nom_de_famille'] + ' ')
        if float(resultatJ1) > 1 or float(resultatJ1) < 0:
            print(" Veuillez rentrer 1 pour une victoire , 0 pour une défaite ou 0.5 pour une égalité. ")
        resultatJ1 = float(resultatJ1)
        resultatJ2 = 1 - resultatJ1
        print(f"Les résultats du match sont: {resultatJ1} : {joueur1['prenom']} et {resultatJ2} : {joueur2['prenom']}")
        return resultatJ1, resultatJ2

    @staticmethod
    def question_start_stop(n_tour_actualy):
        """ Question dans la views match pour print la question """
        if n_tour_actualy != 1:
            print(f"Le tour  {n_tour_actualy-1} est terminé. ")

        question = input(f" Voulez-vous commencer le tour {n_tour_actualy} [ o pour oui ]  ou quitter le programme maintenant [ N pour non ]? 🚦 [o/N] ")
        question = question.strip().lower()
        if question.startswith('n') or question == '':
            print("Vous avez décidé de quitter le programme ! ")
            SystemExit()
        else:
            print("Répondez par 'o' ou 'n'")
        return question
