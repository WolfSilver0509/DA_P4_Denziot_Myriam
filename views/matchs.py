from pprint import pprint

class ViewMatchs():
  """Affichage Matchs en view"""

  @staticmethod 
  def indicate_results(joueur1, joueur2):
    print ( f" Rentrez les résultats du match entre le  {joueur1['prenom']}  {joueur1['nom_de_famille']} et le {joueur2['prenom']} {joueur2['nom_de_famille']} : ")
    resultatJ1 = input('Résultat de '+joueur1['prenom']+' '+joueur1['nom_de_famille'] + ' ')
    resultatJ2 = input('Résultat de '+joueur2['prenom']+' '+joueur2['nom_de_famille'] + ' ')

    print(f"Les résultats de ce match sont : {resultatJ1} pour {joueur1['prenom']} et {resultatJ2} pour {joueur2['prenom']} ")
    return resultatJ1, resultatJ2


    