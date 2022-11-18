
# menu_options = {
#   1: '➕ 🧞 Liste des joueurs par ordre alphabétique',
#   2: '📋Liste des joueurs par classement ',
#   3: '💢 Listes de tous les tournois',
#   4: 'Exit',}

class MenuRapport():
  """Menu Rapport dans view menu repport """
  def menu_option_tournoi(self):
    menu_options_par_tournois = {
      1: '➕♟Listes joueurs par tournois par ordre alphabétique ♟ ♟️',
      2: '📋♟Listes joueurs par tournois par classement ♟ ♟',
      3: '📋 Listes de tous les tour par tournois',
      4: '♟ Listes de tous les matchs par tournois',
      5: 'Retour au menu', }

    for key in menu_options_par_tournois.keys():
      print (key, '--', menu_options_par_tournois[key] )

    option = int(input('Entrer votre choix : '))
    return option

  # if __name__=='__menu_option_tournoi__':
  #     while(True):
  #         menu_option_tournoi()
  #         option = ''
  #         try:
  #             option = int(input('Entrer votre choix : '))
  #         except:
  #             print('Mauvaise entrée. Veuillez entrer un nombre ...')
  #         if option == 1:
  #           controller = PlayerController()
  #           controller.add_player()
  #         elif option == 2:
  #           print('C\'est fini ! ')
  #           exit()
  #         else:
  #           print('Choix Invalide.S\'il vous plait entrer un nombre entre 1 et 4.')
