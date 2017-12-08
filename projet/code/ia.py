#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#TODO: changer le nom de ce module ?

import time
SCORE_MAX = float("inf") # représente l'infini
DEBUG = False

########## Fonction d'évaluation ##########
#
def eval_line(L, n):
    """Param : une liste L, la taille du jeu n
    renvoie la valeur d'un pseudo alignement (1,2,ou3) sur la ligne L"""
    C=0
    C_N=0
    for elem in L:
        if elem == None:
            C_N += 1
        else:
            C += elem
    if C_N + C == n or C ==0:
        res = n-C_N
    else:
        res = 0
    return res

#print(eval_line([1,None,None,None],4))

def eval(game): #applique la fonction eval_line sur chaque ligne du jeu + les diagonales.
    evaluation = 0
    board = game.board
    for k in range(game.size):
        for i in range(game.size):
            line1 = [board[i][l][k] for l in range(game.size)]
            line2 = [board[l][i][k] for l in range(game.size)]
        line3 = [board[l][l][k] for l in range(game.size)]
        line4 = [board[l][game.size-1-l][k] for l in range(game.size)]
        evaluation = eval_line(line1, game.size)+eval_line(line2, game.size)+eval_line(line3, game.size)+eval_line(line4,game.size)
    return evaluation

#
########## MINIMAX ##########


########## MINIMAX ##########
#
def minimax(game, depth):
    """

    :param n: Profondeur maximale de l'arbre
    :return: Retourne e score de l'état de jeu "game"
    """
    best_score_yet = -SCORE_MAX # Pour l'instant le meilleur score est la valeur minimale
    turn = ()

    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                if game.bag != {}:  # traite le cas si le sac est vide : on est à la fin du jeu : l'IA ne peut pas choisir de pièce pour le joueur
                    for (num_piece, char_piece) in game.bag.items():
                        game.play_turn((x, y), num_piece)
                        val_child = val_min(game, depth)
                        if DEBUG:
                            print("pour la coord {} {} la caractéristique {}, valchild = {}".format(x, y, num_piece, val_child))
                        game.undo_turn()

                        if val_child >= best_score_yet: # J'ai (raph) mis un égal ici pour qu'il y ait au moins un coup à jouer
                            best_score_yet = val_child
                            turn = ((x, y), num_piece)
                else: # l'IA ne fait que poser la pièce sans en proposer une au joueur
                    return minimax_values_last_piece(game, (x, y))
    return turn

def val_min(game, depth):
    if game.win:
        return SCORE_MAX

    #TODO: à voir pour le game.end
    if game.end or depth == 0:
        return eval(game)


    vmin = SCORE_MAX
    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                if game.bag != {}: # traite la fin d'une partie, qd y a plus de pièce dans le sac
                    for (num_piece, char_piece) in game.bag.items():
                        game.play_turn((x, y), num_piece)
                        val_child = val_max(game, depth - 1)
                        vmin = min(vmin, val_child)
                        game.undo_turn()

                        
                else:
                    return minimax_values_last_piece(game, (x, y))
                    
    return vmin


def val_max(game, depth):
    if game.win:
        return -SCORE_MAX

    # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return -eval(game)

    vmax = -SCORE_MAX
    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                if game.bag != {}: # traite la fin d'une partie, qd y a plus de pièce dans le sac
                    for (num_piece, char_piece) in game.bag.items():
                        game.play_turn((x, y), num_piece)
                        val_child = val_min(game, depth - 1)
                        vmax = max(vmax, val_child)
                        game.undo_turn()
                        
                else:
                    return -minimax_values_last_piece(game, (x, y))
    return vmax

def minimax_values_last_piece(game, coord):
    res = SCORE_MAX

    # game.play_piece(coord)
    # game.turns_played.append((coord, None))
    # game.select

    game.play_turn(coord, None)

    # Comme c'est la dernière pièce, pas besoin d'appeler ni
    # val_min ni val_max, il faut juste vérifier si il y a un alignement
    if game.win:
        res = SCORE_MAX
    else: # S'il n'y a pas dalignement, alors forcément on arrive sur un match nul
        # en effet, on vient de poser la dernière pièce sur la dernière case
        # disponible du plateau de jeu
        res = 0

    game.undo_turn()

    return res



#
########## FIN DU MINIMAX ##########

########## ALPHA BETA ##########
#
def alphabeta(game, depth, alpha, beta):
    best_score_yet = -SCORE_MAX # Pour l'instant le meilleur score est la valeur minimale
    turn = ()

    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_min_AB(game, depth, alpha, beta)
                    game.undo_turn()

                    if val_child > best_score_yet:
                        best_score_yet = val_child
                        turn = ((x, y), num_piece)
    return turn
    

def val_min_AB(game, depth, alpha, beta):
    if game.win:
        return SCORE_MAX

    # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return eval(game)

    vmin = SCORE_MAX
    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_max_AB(game, depth - 1, alpha, beta)
                    vmin = max(val_child, vmin)
                    if alpha >= vmin:
                        return vmin
                    beta = min(beta, vmin)
                    game.undo_turn()
    return vmin
    
    
def val_max_AB(game, depth, alpha, beta):
    if game.win:
        return -SCORE_MAX

    # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return eval(game)

    vmax = -SCORE_MAX
    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_min_AB(game, depth - 1, alpha, beta)
                    vmax = min(val_child, vmax)
                    if vmax >= beta:
                        return vmax
                    alpha = max(alpha, vmax)
                    game.undo_turn()
    return vmax
                    
  

    


