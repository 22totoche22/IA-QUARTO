#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#TODO: changer le nom de ce module ?

import time
SCORE_MAX = float("inf") # représente l'infini
DEBUG = False

########## Fonction d'évaluation ##########
#
def eval(game):
    return 0
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
                    game.play_piece((x,y))
                    game.selected_piece = None
                    val_child = val_min(game, depth)
                    game.undo_turn()
                    if val_child >= best_score_yet:
                        best_score_yet = val_child
                        turn = ((x,y), None)
    return turn

def val_min(game, depth):
    if game.win:
        return SCORE_MAX

    #TODO: àà voir pour le game.end
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
                else :
                    game.play_piece((x,y))
                    game.selected_piece = None
                    val_child = val_max(game, depth - 1)
                    vmin = min(vmin, val_child)
                    game.undo_turn()
                    
    return vmin


def val_max(game, depth):
    if game.win:
        return -SCORE_MAX

    # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return eval(game)

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
                else :
                    game.play_piece((x,y))
                    game.selected_piece = None
                    val_child = val_min(game, depth - 1)
                    vmax = max(vmax, val_child)
                    game.undo_turn()
                    # TODO : code à factoriser car répétitions
            
          
    return vmax
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
                    
  

    


