from controllers.PlayerController import PlayerController
from controllers.TournoisController import TournoisController


menu_options = {
    1: '➕ 🧞‍♀️ Nouveau Joueur',
    2: '📋Listes des joueurs',
    3: '➕♟️ Nouveau Tournois♟ ♟️',
    4: '📋Listes des tournois',
    5: 'Exit',
}

def main():
  for key in menu_options.keys():
    print (key, '--', menu_options[key] )

if __name__=='__main__':
    while(True):
        main()
        option = ''
        try:
            option = int(input('Entrer votre choix : '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
          controller = PlayerController()
          controller.add_player()
        elif option == 2:
          controller = PlayerController()
          controller.list_players()
        elif option == 3:
          controller = TournoisController()
          controller.add_tournament()
        elif option == 4:
          controller = TournoisController()
          controller.list_tournois()
        elif option == 5:
          print('C\'est fini ! ')
          exit()
        else:
          print('Choix Invalide.S\'il vous plait entrer un nombre entre 1 et 4.')

if __name__ == 'main':
    main()
  # exécute la fonction main (l5) a partir du moment ou dans la console on lance le script pyhton main.py 