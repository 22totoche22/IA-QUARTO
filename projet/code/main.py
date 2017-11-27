import ui_projet
import game


if __name__ == "__main__":
    launched_game = game.Game(game.SIZE)

    # Select a basic piece in order to play the first move
    launched_game.selected_piece = launched_game.bag[0]

    # Beginning of the game loop
    while not launched_game.end:
        print("Sélectionnez la coordonnées ou vous voulez placer la piece ({}) : ".format(launched_game.selected_piece))
        x = input("x coord = ")
        y = input("y coord = ")

