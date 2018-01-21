#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ia
from random import randrange
SCORE_MAX = float("inf")  # infinity number
DEBUG = False

########## Heuristic fonction ##########

def eval_line(L, n, p):
    """
    L is a list of 0, 1 or None. Returns the number of aligned digits (0 or 1) if the digit p fill a None place of the
    list.
    :param L: list
    :param n: size of the list
    :param p: a digit (0 or 1)
    :return: res : int
    """
    c = 0  # sums digits
    c_n = 0  # counts Nones
    for i, elem in enumerate(L):
        if elem is None:
            c_n += 1
        else:
            c += elem
    if c_n + c == n or c == 0:
        if 0 < c_n < n:
            i = 0
            elem = L[i]
            while elem is None:
                i += 1
                elem = L[i]
            if p == elem:
                res = -(n - c_n + 1)
            else:
                res = n - c_n
        else:
            res = n - c_n
    else:
        res = 0
    return res


def eval(game):
    """
    Makes the sum of the values of eval_line for each lines of the board. This is the heuristic function.
    :param game:
    :return: evaluation : int
    """
    evaluation = 0
    board = game.board
    for k in range(game.size):
        p = game.selected_piece.charact[k]
        for i in range(game.size):
            line1 = [board[i][j][k] for j in range(game.size)]
            line2 = [board[j][i][k] for j in range(game.size)]
            evaluation = evaluation + eval_line(line1, game.size, p) + eval_line(line2, game.size, p)
        line3 = [board[j][j][k] for j in range(game.size)]  # diagonals
        line4 = [board[j][game.size-1-j][k] for j in range(game.size)]
        evaluation = evaluation + eval_line(line3, game.size, p) + eval_line(line4, game.size, p)
    return evaluation


########### At the end of the game ###########

def minimax_values_last_piece(game, coord):
    """
    Function which evaluates a final node (when only putting the selected piece on the board is necessary) and which
    plays the turn.
    :param game:
    :param coord:
    :return: evaluation of the position : int
    """
    game.play_turn(coord, None)
    if game.win:
        res = SCORE_MAX
    else:  # no winner and all pieces have been used, so there is no alignment.
        res = 0
    game.undo_turn()

    return res


########## MINIMAX ##########

def minimax(game, depth, player=1):
    """
    Minimax algorithm for the Quarto game
    :param:
     - game : a game state
     - depth : where to stop in the tree of possibilities
     - player : 1 = max        -1 = min
    :return: Returns a turn and its value by the heuristic function
    """

    if game.win:  # the final nodes
        return None, -1 * player * SCORE_MAX

    if game.end or depth == 0:  # the final nodes
        return None, -1 * player * eval(game)

    turn = ()

    if player == 1:  # MAX node
        vmax = -SCORE_MAX
        # all the sons of the node will be browsed
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = minimax(game, depth-1, -1)
                            game.undo_turn()
                            if val_child >= vmax:
                                vmax = val_child
                                turn = (x, y), num_piece
                    else:  # the last turn
                        turn = ((x, y), None)
                        v = -minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmax
    else:  # MIN node
        vmin = SCORE_MAX
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = minimax(game, depth-1, 1)
                            game.undo_turn()
                            if val_child <= vmin:
                                vmin = val_child
                                turn = (x, y), num_piece
                    else:  # the last turn
                        turn = ((x, y), None)
                        v = minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmin




########## ALPHA BETA ##########

def alphabeta(game, depth, player=1, alpha=-float("inf"), beta=float("inf")):
    """
    AlphaBeta algorithm for the Quarto game
    :param:
     - game : a game state
     - depth : where to stop in the tree of possibilities
     - player : 1 = max        -1 = min
     - alpha = best score for maximizer
     - beta = best score for minimizer
    :return: returns a turn and its value by the heuristic function
    """

    if game.win:  # the final nodes
        return None, -1 * player * SCORE_MAX

    if game.end or depth == 0:  # the final nodes
        return None, -1 * player * eval(game)

    if player == 1:  # MAX node
        vmax = -SCORE_MAX
        turn = ()
        # all the sons of the node will be browsed
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = alphabeta(game, depth-1, -1, alpha, beta)
                            game.undo_turn()
                            if val_child > vmax:
                                vmax = val_child
                                turn = (x, y), num_piece
                            alpha = max(alpha, vmax)
                            if alpha >= beta:  # cut béta
                                return turn, vmax
                    else:  # the last turn
                        turn = ((x, y), None)
                        v = minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmax
    else:  # MIN node
        vmin = SCORE_MAX
        turn = ()
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = alphabeta(game, depth-1, 1, alpha, beta)
                            game.undo_turn()
                            if val_child < vmin:
                                vmin = val_child
                                turn = (x, y), num_piece
                            beta = min(beta, vmin)
                            if alpha >= beta:  # alpha cut
                                return turn, vmin
                    else:  # the last turn
                        turn = ((x, y), None)
                        v = -minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmin




######## enhancement of the alphabeta algorithm #######

def select_best_turn(launched_game):
    """
    Enhancement of the alphabeta algorithm
    :param launched_game:
    :return: a turn
    """
    #  the first turn is random
    if len(launched_game.bag) == launched_game.size ** 2 - 1:
        num_piece = randrange(launched_game.size ** 2 - 1)
        while num_piece == launched_game.selected_piece:
            num_piece = randrange(launched_game.size ** 2 - 1)
        coord = (randrange(launched_game.size), randrange(launched_game.size))
        return coord, num_piece
    #  the depth is variable during the whole game
    elif len(launched_game.bag) >= 2 ** launched_game.size - launched_game.size:
        do_the_depth = 2
    elif 2 ** launched_game.size - launched_game.size > len(launched_game.bag) >= 6:
        do_the_depth = 3
    else:
        do_the_depth = 6
    turn, v = ia.alphabeta(launched_game, do_the_depth)
    if turn == ():  # gère le cas problèmatique non résolu de turn = ()
        print("turn = () donc hasard")
        num = randrange(launched_game.size ** 2)
        while num not in launched_game.bag:
            num = randrange(launched_game.size ** 2)
        (x, y) = (randrange(launched_game.size), randrange(launched_game.size))
        while launched_game.board[x][y] != [None] * launched_game.size:
            (x, y) = (randrange(launched_game.size), randrange(launched_game.size))
        turn = ((x, y), num)
    return turn
