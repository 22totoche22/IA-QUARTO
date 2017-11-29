#TODO: changer le nom de ce module ?

SCORE_MAX = 1000000000 # 1 milliard représente l'infini, TODO: à changer

def minimax(n, game):
    """

    :param n: Profondeur maximale de l'arbre
    :return: Retourne e score de l'état de jeu "game"
    """

    """
    if n==0 or joueurcourrentagagné:
        return scoremax
        
    Pour tout les coups possibles:
        jouer le coup
        évaluer le score de l'état de jeu actuel, le mettre dans score
        undo le coup
        
        si ce score est meilleur que tout ceux visiter alors best_score = score
    
    return best_score
        
        
    """

    if n == 0: #or best_score_yet >= SCORE_MAX:
        return SCORE_MAX

    best_score_yet = -SCORE_MAX # Pour l'instant le meilleur score est la valeur minimale

    for x in game.size:
        for y in game.size:
            if game.board[x][y][0] is None:
                for (num_piece, char_piece) in game.bag.items():
                    game.play_turn((x, y), num_piece)

                    intermediate_score = minimax(n-1, game)

                    game.undo_turn()

                    if intermediate_score > best_score_yet:
                        best_score_yet = intermediate_score






