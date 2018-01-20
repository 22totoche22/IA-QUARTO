#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import piece
from collections import deque


# Globals variables
PLAYER_A = 1
PLAYER_B = -1
SIZE = 4

# In order to print things in the console to help with debugging
DEBUG = True


class Game:
    def __init__(self, size):
        """
        A Game represents a state of game : a size, a board, a bag of pieces (dic), a current player, a selected
        piece (None first), win (bool), end (bool), coords, coord
        :param size (int):
        """
        self.size = size
        self.board = [[[None for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]  # 3D board
        self.bag = {}
        self.init_full_bag()
        self.current_player = PLAYER_A
        self.selected_piece = None
        self.win = False  # True if a player wins : "Quarto!"
        self.end = self.win or self.is_board_filled()  # In a further development, game.end will have other functions
        self.coords = [(i, j) for i in range(self.size) for j in range(self.size)]  # list of all possibles coordinates
        self.coord = None  # couple, initialized to None
        self.turns_played = None # a LIFO that sums up the played turns

    def init_full_bag(self):
        """
        Initializes the bag at the beginning of the game : all pieces are present in the bag
        """
        for i in range(2**self.size):
            self.bag[i] = piece.Piece(i, self.size)  # adds the piece in the bag, the key equals to the binary number

    def is_board_filled(self):
        """
        Verifies if all the position of the board are occupied by a piece
        :return: boolean
        """
        no_piece = [None for _ in range(self.size)]
        for line in self.board:
            if no_piece in line:  # if there is an empty place, the board is not filled
                return False
        return True

    def select_piece(self, num):
        """
        Selects the piece whom number is num (decimal) as the game.selected_piece of the game.current_player and removes
        it from the bag.
        :param num : int between 0 and game.size**2:
        """
        piece = self.bag[num]
        del self.bag[num]
        self.selected_piece = piece

    def play_piece(self, coord):
        """
        Puts the game.selected_piece at coordinates coord. Then, updates game.win and game.end
        :param coord: a couple
        """
        x, y = coord[0], coord[1]
        for k in range(self.size):
                self.board[x][y][k] = self.selected_piece.charact[k]

        #  update the "win" state of the game
        self.win = self.full_row2((x, y))

        #  Update the "end state of the game
        self.end = self.win or self.is_board_filled()

    def play_turn(self, coord, num):
        """
        Basic method to play a turn. Then, updates game.win, game.end, game.current_player
        :param coord: coordinate where the selected_piece will be placed
        :param num: the representative number of the piece which will be selected for the other player
        """
        self.play_piece(coord)
        if num is None:
            self.selected_piece = None
        else:
            self.select_piece(num)
        self.win = self.full_row2(coord)
        self.end = self.win
        self.turns_played.append((coord, num))
        self.current_player *= -1

    def undo_turn(self):
        """
        Go back to the last game's state (from the other player)
        Assumes that play_turn has already been called
        """
        (coord, last_selected_piece) = self.turns_played.pop()
        self.selected_piece = piece.Piece(self.turns_played[-1][1], self.size)
        if last_selected_piece is not None:
            self.bag[last_selected_piece] = piece.Piece(last_selected_piece, self.size)
        self.board[coord[0]][coord[1]] = [None for _ in range(self.size)]
        self.current_player *= -1

    def init_from_turns_played(self, list_of_turns):
        """
        Init the board from a list of turns played by different players
        :param list_of_turns: list
        """
        self.select_piece(list_of_turns[0][1])
        for i in range(1, len(list_of_turns)):
            x = list_of_turns[i][0][0]
            y = list_of_turns[i][0][1]
            self.play_turn((x, y), list_of_turns[i][1])

    def full_row2(self, coord):
        """
        Verifies whether the lines crossing coord make alignment or not
        :param coord:
        :return: boolean
        """
        board = self.board
        n = self.size
        i, j = coord[0], coord[1]
        res = False
        for k in range(n):
            line_h = [board[i][m][k] for m in range(n)]
            line_v = [board[m][j][k] for m in range(n)]
            diag1 = [None]*n
            diag2 = [None]*n
            if i == j:
                diag1 = [board[m][m][k] for m in range(n)]
            if i + j == n - 1:
                diag2 = [board[m][n-1-m][k] for m in range(n)]
            res = res or (n in [align_line(line_h, n), align_line(line_v, n), align_line(diag1, n), align_line(diag2, n)])
        return res

    def __repr__(self):
        """
        Returns a display of a state of the game
        :return: (String) res
        """
        res = ""
        res += "Pièce sélectionnée par le joueur adverse : " + str(self.selected_piece) + "\n"*2
        for y_board in range(self.size):
            for i_layer in range(self.size):
                for x_board in range(self.size):
                    res += "." if self.board[x_board][y_board][i_layer] is None else str(self.board[x_board][y_board][i_layer])
                res += "\t"*2
            res += "\n"
        res += "\n"
        res += "pièces restantes dans le sac : \n"
        for p in self.bag.values():
            res += str(p) + "\n"
        return res


def align_line(L, n):
    """
    L is a list of 0, 1 or None. Returns the number of aligned digits (0 or 1)
    :param L: a list
    :param n: size of L
    :return:
    """
    C = 0
    C_N = 0
    for i, elem in enumerate(L):
        if elem == None:
            C_N += 1
        else:
            C += elem
    if C_N + C == n or C == 0:
        res = n - C_N
    else:
        res = 0
    return res
