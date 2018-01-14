#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#TODO: changer le nom de ce module ?

import time
SCORE_MAX = float("inf") # représente l'infini
DEBUG = False

########## Fonction d'évaluation ##########
#
def eval_line(L, n, p):
    """Param : une liste L, la taille du jeu n
    renvoie la valeur d'un pseudo alignement (1,2,ou3) sur la ligne L"""
    C=0
    C_N=0
    for i, elem in enumerate(L):
        if elem == None:
            C_N += 1
        else:
            C += elem
    if C_N + C == n or C ==0:
        if 0 < C_N < n:
            i = 0
            elem = L[i]
            while elem == None :
                i += 1
                elem = L[i]
            if p == elem:
                res = -(n - C_N + 1)
            else :
                res = n - C_N
        else :
            res = n - C_N
    else:
        res = 0
    return res

#print(eval_line([1,1,1,1],4, 1))

def eval(game): #applique la fonction eval_line sur chaque ligne du jeu + les diagonales.
    evaluation = 0
    board = game.board
    for k in range(game.size):
        p = game.selected_piece.charact[k]
        for i in range(game.size):
            line1 = [board[i][j][k] for j in range(game.size)]
            line2 = [board[j][i][k] for j in range(game.size)]
            evaluation = evaluation + eval_line(line1, game.size, p) + eval_line(line2, game.size, p)
        line3 = [board[j][j][k] for j in range(game.size)]
        line4 = [board[j][game.size-1-j][k] for j in range(game.size)]
        evaluation = evaluation + eval_line(line3, game.size, p) + eval_line(line4,game.size, p)
    return evaluation


########### Fonction pour quand le tableau est presque rempli ###########
#

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
##########################################################################

########## MINIMAX ##########
#
def minimax(game, depth, player=1):
    """
    :param:
     - game : a game state
     - depth : where to stop in the tree of possibilities
     - player : 1 = max        -1 = min
    :return: Retourne e score de l'état de jeu "game"
    """

    if game.win:
        return (None, -1 * player * SCORE_MAX)

        # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return (None, -1 * player * eval(game))

    # best_score_yet = -1 * player * SCORE_MAX

    turn = ()
    # Si on est dans un noeud max
    if player == 1:
        # On itnitialise le meilleur score pour linstant
        vmax = -SCORE_MAX
        #On parcourt toutes les possibilités
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
                    else:
                        # l'IA ne fait que poser la pièce sans en proposer une au
                        # joueur
                        turn = ((x, y), None)
                        v = -minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmax
    else:
        # On itnitialise le meilleur score pour linstant
        vmin = SCORE_MAX
        #On parcourt toutes les possibilités
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
                    else:
                        # l'IA ne fait que poser la pièce sans en proposer une au
                        # joueur
                        turn = ((x, y), None)
                        v = minimax_values_last_piece(game, (x, y))
                        return turn, v
        return turn, vmin
############################# Fin Minimax #############################



########## ALPHA BETA ##########
#
def alphabeta(game, depth, player=1, alpha = -float("inf"), beta = float("inf")):
    """
    :param:
     - game : a game state
     - depth : where to stop in the tree of possibilities
     - player : 1 = max        -1 = min
     - alpha = best score for maximizer
     - beta = best score for minimizer
    :return: Retourne e score de l'état de jeu "game"
    """

    if game.win:
        return (None, -1 * player * SCORE_MAX)

        # TODO: à voir pour le game.end
    if game.end or depth == 0:
        return (None, -1 * player * eval(game))

    # best_score_yet = -1 * player * SCORE_MAX

    # Si on est dans un noeud max
    if player == 1:
        # On itnitialise le meilleur score pour linstant
        vmax = -SCORE_MAX
        turn = ()
        #On parcourt toutes les possibilités
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = alphabeta(game, depth-1, -1, alpha, beta)
                            game.undo_turn()

                            #vmax = max(vmax, val_child)
                            #if vmax >= beta:
                                #turn = (x,y), num_piece
                                #return turn, vmax
                            #alpha = max(alpha, vmax)

                            if val_child > vmax:
                                vmax = val_child
                                turn = (x, y), num_piece
                                #print("\t" * (2 - depth), 1, temporary_turn, val_child, alpha, beta)

                            alpha = max(alpha, vmax)
                            # Coupure BETA
                            if alpha >= beta:
                                return turn, vmax
                    else:
                        # l'IA ne fait que poser la pièce sans en proposer une au
                        # joueur
                        turn = ((x, y), None)
                        v = minimax_values_last_piece(game, (x, y)) # avant c'était un - mais ça semble mieux marcher comme ça
                        return turn, v
        return turn, vmax
    else:
        # On itnitialise le meilleur score pour linstant
        vmin = SCORE_MAX
        turn = ()
        #On parcourt toutes les possibilités
        for x in range(game.size):
            for y in range(game.size):
                if game.board[x][y][0] is None:
                    if game.bag != {}:
                        for (num_piece, char_piece) in game.bag.items():
                            game.play_turn((x, y), num_piece)
                            temporary_turn, val_child = alphabeta(game, depth-1, 1, alpha, beta)
                            game.undo_turn()

                            # vmin = min(vmin, val_child)
                            # if alpha >= vmin:
                                # turn = (x,y), num_piece
                                # return turn, vmin
                            # beta = min(beta, vmin)

                            if val_child < vmin:
                                vmin = val_child
                                turn = (x, y), num_piece
                                #print("\t" * (2 - depth), -1, temporary_turn, val_child, alpha, beta)

                            beta = min(beta, vmin)

                            # Coupure alpha
                            if alpha >= beta:
                                return turn, vmin
                    else:
                        # l'IA ne fait que poser la pièce sans en proposer une au
                        # joueur
                        turn = ((x, y), None)
                        v = -minimax_values_last_piece(game, (x, y)) # avant c'était un + mais ça semble mieux marcher comme ça
                        return turn, v
        return turn, vmin

############ FIN ALPHA BETA ################









############################## POUBELLE ############################


#
#
# ########## MINIMAX ##########
# #
# def minimax(game, depth):
#     """
#
#     :param n: Profondeur maximale de l'arbre
#     :return: Retourne e score de l'état de jeu "game"
#     """
#     best_score_yet = -SCORE_MAX # Pour l'instant le meilleur score est la valeur minimale
#     turn = ()
#
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 if game.bag != {}:  # traite le cas si le sac est vide : on est à la fin du jeu : l'IA ne peut pas choisir de pièce pour le joueur
#                     for (num_piece, char_piece) in game.bag.items():
#                         game.play_turn((x, y), num_piece)
#                         val_child = val_min(game, depth)
#                         if DEBUG:
#                             print("pour la coord {} {} la caractéristique {}, valchild = {}".format(x, y, num_piece, val_child))
#                         game.undo_turn()
#
#                         if val_child >= best_score_yet: # J'ai (raph) mis un égal ici pour qu'il y ait au moins un coup à jouer
#                             best_score_yet = val_child
#                             turn = ((x, y), num_piece)
#                 else: # l'IA ne fait que poser la pièce sans en proposer une au joueur
#                     return ((x, y), None)
#     return turn
#
# def val_min(game, depth):
#     if game.win:
#         return SCORE_MAX
#
#     #TODO: à voir pour le game.end
#     if game.end or depth == 0:
#         return eval(game)
#
#
#     vmin = SCORE_MAX
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 if game.bag != {}: # traite la fin d'une partie, qd y a plus de pièce dans le sac
#                     for (num_piece, char_piece) in game.bag.items():
#                         game.play_turn((x, y), num_piece)
#                         val_child = val_max(game, depth - 1)
#                         vmin = min(vmin, val_child)
#                         game.undo_turn()
#
#
#                 else:
#                     return minimax_values_last_piece(game, (x, y))
#
#     return vmin
#
#
# def val_max(game, depth):
#     if game.win:
#         return -SCORE_MAX
#
#     # TODO: à voir pour le game.end
#     if game.end or depth == 0:
#         return -eval(game)
#
#     vmax = -SCORE_MAX
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 if game.bag != {}: # traite la fin d'une partie, qd y a plus de pièce dans le sac
#                     for (num_piece, char_piece) in game.bag.items():
#                         game.play_turn((x, y), num_piece)
#                         val_child = val_min(game, depth - 1)
#                         vmax = max(vmax, val_child)
#                         game.undo_turn()
#
#                 else:
#                     return -minimax_values_last_piece(game, (x, y))
#     return vmax
#
#
#
#
# #
# ########## FIN DU MINIMAX ##########
#
# ########## ALPHA BETA ##########
# #
# def alphabeta(game, depth, alpha, beta):
#     best_score_yet = -SCORE_MAX # Pour l'instant le meilleur score est la valeur minimale
#     turn = ()
#
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 for (num_piece, char_piece) in game.bag.items():
#                     game.play_turn((x, y), num_piece)
#                     val_child = val_min_AB(game, depth, alpha, beta)
#                     game.undo_turn()
#
#                     if val_child > best_score_yet:
#                         best_score_yet = val_child
#                         turn = ((x, y), num_piece)
#     return turn
#
#
# def val_min_AB(game, depth, alpha, beta):
#     if game.win:
#         return SCORE_MAX
#
#     # TODO: à voir pour le game.end
#     if game.end or depth == 0:
#         return eval(game)
#
#     vmin = SCORE_MAX
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 for (num_piece, char_piece) in game.bag.items():
#                     game.play_turn((x, y), num_piece)
#                     val_child = val_max_AB(game, depth - 1, alpha, beta)
#                     vmin = max(val_child, vmin)
#                     if alpha >= vmin:
#                         return vmin
#                     beta = min(beta, vmin)
#                     game.undo_turn()
#     return vmin
#
#
# def val_max_AB(game, depth, alpha, beta):
#     if game.win:
#         return -SCORE_MAX
#
#     # TODO: à voir pour le game.end
#     if game.end or depth == 0:
#         return eval(game)
#
#     vmax = -SCORE_MAX
#     for x in range(game.size):
#         for y in range(game.size):
#             if game.board[x][y][0] is None:
#                 for (num_piece, char_piece) in game.bag.items():
#                     game.play_turn((x, y), num_piece)
#                     val_child = val_min_AB(game, depth - 1, alpha, beta)
#                     vmax = min(val_child, vmax)
#                     if vmax >= beta:
#                         return vmax
#                     alpha = max(alpha, vmax)
#                     game.undo_turn()
#     return vmax
#
  

    


