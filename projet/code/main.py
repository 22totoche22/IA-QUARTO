import time
import game
import ia

t1 = time.time()
if __name__ == "__main__":
    launched_game = game.Game(game.SIZE)
    # launched_game.init_from_turns_played([[None, 0], [(0,0), 1], [(2,2), 2]])
    ## DEBUT MAIN AVEC IA
    #
    while not launched_game.end:
        if launched_game.current_player == 1:
            print("\n\n{:=^50}".format("Tour du joueur " + str(launched_game.current_player)))
            print("Sélectionnez la coordonnées où vous voulez placer la pièce ({}) : ".format(launched_game.selected_piece))
            print()
            print(launched_game)
            x = int(input("x coord = "))
            y = int(input("y coord = "))

            # TODO : Verify if the user input is correct

            print("Sélectionnez la pièce que jouera l'autre joueur ou tapez 'Quarto!' si vous pensez avoir gagné\n")
            for (index, el) in launched_game.bag.items():
                print(el)
            # TODO: si le joueur ecrit quarto! vérifier qu'il a gagné
            i = int(input("Numéro de la pièce = "))

            launched_game.play_turn((x, y), i)
        else:
            print("\n\n{:=^50}".format(" Tour de Charles-Maurice "))

            # TODO: augmenter la profondeur lorsqu'on arrive vers une grille plus remplie
            # (coord, num_piece) = ia.alphabeta(launched_game, 3, -float("inf"), float("inf"))
            (coord, num_piece) = ia.minimax(launched_game, 3)
            print(coord, num_piece)
            
            launched_game.play_turn(coord, num_piece)

            print(time.time()-t1)

        print(launched_game.turns_played)
        print(launched_game)


    # Beginning of the game loop
    # while not launched_game.end:
    #     print("\n\n{:=^50}".format("Tour du joueur "+str(launched_game.current_player)))
    #     print("Sélectionnez la coordonnées où vous voulez placer la pièce ({}) : ".format(launched_game.selected_piece))
    #     print()
    #     print(launched_game)
    #     x = int(input("x coord = "))
    #     y = int(input("y coord = "))
    #
    #     # TODO : Verify if the user input is correct
    #
    #     # launched_game.play_piece((x,y))
    #     # print(launched_game)
    #     #
    #     # launched_game.end = launched_game.full_row((x,y),launched_game.size)
    #
    #     print("Sélectionnez la pièce que jouera l'autre joueur ou tapez 'Quarto!' si vous pensez avoir gagné\n")
    #     for (index, el) in launched_game.bag.items():
    #         print(el)
    #     # TODO: si le joueur ecrit quarto! vérifier qu'il a gagné
    #     i = int(input("Numéro de la pièce = "))
    #     # launched_game.select_piece(i)
    #     # launched_game.current_player *= -1
    #
    #     launched_game.play_turn((x, y), i)

    print("QUARTO")

