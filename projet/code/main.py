import ui_projet
import game


if __name__ == "__main__":
    launched_game = game.Game(game.SIZE)

    # Select a basic piece in order to play the first move
    launched_game.select_piece(0)

    # Beginning of the game loop
    while not launched_game.end:
        print("Sélectionnez la coordonnées où vous voulez placer la pièce ({}) : ".format(launched_game.selected_piece))
        print(launched_game.board)
        x = int(input("x coord = "))
        y = int(input("y coord = "))


        launched_game.play_piece((x,y))
        print(launched_game.board)

        launched_game.end = launched_game.full_row((x,y),launched_game.size)

        print("Sélectionnez la pièce")
        print(launched_game.bag)
        i = int(input("Numéro de la pièce = "))
        launched_game.select_piece(i)

    print("QUARTO")