# -*- coding: utf-8 -*-
import game
import ia
from collections import deque
from random import randrange


# Here is defined 3 Exceptions concerning the bag, the board and the players
class BagError(Exception):
    pass


class BoardError(Exception):
    pass


class PlayerError(Exception):
    pass


class AbandoningError(Exception):
    pass


if __name__ == "__main__":

    launched_game = game.Game(game.SIZE)
    size = launched_game.size

    while True:
        try:
            launched_game.current_player = int(input("{:=^50}".format(" choisissez le premier joueur : ") + "\n\n"
                                                     + "{:=^50}".format(" joueur 1 ou joueur -1 ? ")  + "\n\n"))
            if launched_game.current_player in [1, -1]:
                break
            else:
                raise PlayerError
        except PlayerError:
            print("Veillez choisir seulement entre 1 et -1" + "\n\n")
        except ValueError:
            print("Veillez choisir seulement entre 1 et -1" + "\n\n")

    if launched_game.current_player == 1:
        while True:
            try:
                num = int(input("choisissez la première pièce : "))
                if 0 <= num <= 2**size - 1:
                    break
                else:
                    raise BagError
            except BagError:
                print("Veillez choisir un numéro entre 0 et " + str(size ** 2 - 1))
            except ValueError:
                print("Veillez choisir un numéro entre 0 et " + str(size ** 2 - 1))

    if launched_game.current_player == -1:
        num = randrange(size ** 2)

    launched_game.select_piece(num)
    launched_game.turns_played = deque([(None, launched_game.selected_piece.num)])
    launched_game.current_player *= -1

    while not launched_game.end:

        if launched_game.current_player == 1:
            print("\n\n{:=^50}".format("Tour du joueur " + str(launched_game.current_player)))
            print()
            print(launched_game)
            print("Sélectionnez les coordonnées où vous voulez placer la pièce ({}) : ".format(
                launched_game.selected_piece))
            while True:
                try:
                    x = int(input("x coord = "))
                    y = int(input("y coord = "))
                    if 0 <= x < size and 0 <= y < size and launched_game.board[x][y] == [None]*size:
                        break
                    else:
                        raise BoardError
                except BoardError:
                    print("Ces coordonées ne sont pas sur le plateau")
                except ValueError:
                    print("Veillez saisir des coordonnées entières")
            if launched_game.bag != {}:
                print("Sélectionnez la pièce que jouera l'autre joueur ou tapez 'Quarto!' si vous pensez avoir gagné\n")
                while True:
                    try:
                        i = int(input("Numéro de la pièce = "))
                        if i in launched_game.bag:
                            break
                        else:
                            raise BagError
                    except BagError:
                        print("Cette pièce n'est pas disponible")
                    except ValueError:
                        print("le numéro de la pièce doit être un entier")
            else :
                i = None
            launched_game.play_turn((x, y), i)

        else:
            print("\n\n{:=^50}".format(" Tour de Charles-Maurice "))
            turn = ia.select_best_turn(launched_game)
            print(turn)
            if turn is not None:
                coord, num_piece = turn[0], turn[1]
                print("Charles-Maurice a placé la pièce " + str(launched_game.selected_piece) +
                    " aux coordonnées " + str(coord) + " et vous donne la pièce " + str(num_piece))
                launched_game.play_turn(coord, num_piece)

    if launched_game.win:
        print("{:#^50}".format("!!!!!!! QUARTOOOOO !!!!!"))
    print("#" * 20 + "FIN DU JEU" + "#" * 20)
    print(launched_game.turns_played)
    print(launched_game)
