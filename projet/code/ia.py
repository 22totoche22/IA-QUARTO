#TODO: changer le nom de ce module ?

SCORE_MAX = float("inf") # représente l'infini

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
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_min(game, depth)
                    game.undo_turn()

                    if val_child > best_score_yet:
                        best_score_yet = val_child
                        turn = ((x, y), num_piece)
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
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_max(game, depth - 1)
                    vmin = min(vmin, val_child)
                    game.undo_turn()
    return vmin


def val_max(game, depth):
    if game.win:
        return SCORE_MAX

    # TODO: àà voir pour le game.end
    if game.end or depth == 0:
        return eval(game)

    vmax = -SCORE_MAX
    for x in range(game.size):
        for y in range(game.size):
            if game.board[x][y][0] is None:
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)
                    val_child = val_min(game, depth - 1)
                    vmax = max(vmax, val_child)
                    game.undo_turn()
    return vmax

def eval(game):
    return 0




