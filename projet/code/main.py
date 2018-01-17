
# -*- coding: utf-8 -*-

import time
import game
import ia
from collections import deque
from random import randrange

t1 = time.time()
if __name__ == "__main__":
    launched_game = game.Game(game.SIZE)
    # deque([(None, 3), ((1, 2), 15), ((3, 3), 1), ((2, 2), 7), ((3, 2), 5)])
    # deque([(None, 3), ((1, 2), 15), ((3, 3), 13), ((2, 2), 7), ((3, 2), 11)])
    ## DEBUT MAIN AVEC IA
    # launched_game.select_piece(randrange(launched_game.size))
    launched_game.select_piece(0)
    launched_game.turns_played = deque([(None, launched_game.selected_piece.num)])
    # launched_game.init_from_turns_played([(None, 3), ((1, 2), 15)])
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
            t1 = time.time()
            # TODO: augmenter la profondeur lorsqu'on arrive vers une grille plus remplie

            ((coord, num_piece), v) = ia.alphabeta(launched_game, 3)
            # ((coord, num_piece), v) = ia.minimax(launched_game, 4)
            print(coord, num_piece)

            launched_game.play_turn(coord, num_piece)

            print(time.time()-t1)

    print("{:#^50}".format("!!!!!!! QUARTOOOOO !!!!!"))
    print("#"*20 + "FIN DU JEU" + "#"*20)
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

    

