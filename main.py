from controllers.PlayerController import PlayerController
from controllers.TournoisController import TournoisController


menu_options = {
    1: '➕ 🧞‍♀️ Nouveau Joueur',
    2: '➕♟️ Nouveau Tournois♟ ♟️',
    3: '💢 Reprendre un tournois',
    4: '📋Listes des joueurs par ordre alphabétique',
    5: '📋Listes des joueurs par ordre de classement',
    6: '📋Listes des tournois',
    7: 'Exit',
}


def main():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


if __name__ == '__main__':
    while True:
        main()
        option = input('Entrer votre choix : ')
        try:
            option = int(option)
        except Exception as ex:
            print('Mauvaise entrée. Veuillez entrer un nombre ...')
        if option == 1:
            controller = PlayerController()
            controller.add_player()
        elif option == 2:
            controller = TournoisController()
            controller.add_tournament()
        elif option == 3:
            controller = TournoisController()
            controller.back_up_tournament()
        elif option == 4:
            controller = PlayerController()
            controller.list_players()
        elif option == 5:
            controller = PlayerController()
            controller.list_players_by_rank()
        elif option == 6:
            controller = TournoisController()
            controller.list_tournois()
        elif option == 7:
            print('C\'est fini ! ')
            exit()
        else:
            print('Choix Invalide.S\'il vous plait entrer un nombre entre 1 et 7.')

if __name__ == 'main':
    main()
