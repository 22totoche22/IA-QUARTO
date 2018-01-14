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


class Bag_error(Exception):
    pass


class Cell_error(Exception):
    pass


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
        self.end = False
        self.coords = [(i, j) for i in range(self.size) for j in range(self.size)]  # list of all possibles coordinates
        self.coord = None  # couple, initialized to None
        # self.turns_played = deque([(None, self.selected_piece.num)])

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
        # try :
        #     coord = self.coords[self.coords.index(coord)]
        #     del self.coords[self.coords.index(coord)]
        # except Exception:  # Error if the coordinates "coord" have already been choosen
        #         print(Cell_error("this cell is already taken: Choose an other one"))
        #         x = int(input("x coord = "))
        #         y = int(input("y coord = "))
        #         self.play_piece((x,y))
        for k in range(self.size):
                self.board[x][y][k] = self.selected_piece.charact[k]

        # update the "win" state of the game
        self.win = self.full_row((x, y), self.size)

        # Update the "end state of the game
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
        self.win = self.full_row(coord, self.size)
        # TODO: voir si le joueur à compris qu'il avait gagné et donc le jeu ne sera pas forcément finit dés qu'il y aura 4 pièces alignées
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

    def full_row(self, coord, n):
        """
        Verifies if there is a full horizontal, vertical, or diagonal row of n pieces with the same characteristics
        after putting the piece at t
        :param coord:
        :param n:
        :return:
        """
        #he coordinates(x,y) on the board
        victory = []
        for i in range(self.size):
            layer_i = layer_tab(self.board, i)
            victory.append(row_layer(layer_i, n, coord))
        return True in victory

    def __repr__(self):
        """
        Renvoi un affichage de l'état de jeu courant
        :return: (String) res : représente l'état de jeu
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


def row(list, n): #returns if there is a row of n '1' in a simple list
    compteur_1 = 0
    compteur_0 = 0
    max_compteur_1 = 0
    max_compteur_0 = 0
    for i in list:
        if i == 1:
            compteur_1 += 1
            compteur_0 = 0
            max_compteur_1 = max(compteur_1,max_compteur_1)
            max_compteur_0 = 0
        if i == 0:
            compteur_1 = 0
            compteur_0 += 1
            max_compteur_0 = max(compteur_0,max_compteur_0)
            max_compteur_1 = 0
    return max_compteur_1 == n or max_compteur_0 == n


def layer_tab(board, k):
    """
    Returns the k layer of a 3D board. Does nothing if k >= len(board)
    :param board: a 3D board (list of lists of lists)
    :param k: int
    :return: a 2D board (list of lists)
    """
    n = len(board)
    if k < n:
        layer = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                    layer[i][j] = board[i][j][k]
        return layer



def row_layer(layer,n,coord): #returns True if there is a full horizontal, vertical, or diagonal row of'1' or '0' with the point whose coordinates are (x,y) in the layer, coord is a tuple
    x,y = coord[0], coord[1]
    long = len(layer)
    horizontale = layer[x]
    verticale = vertical(layer,(x,y))
    diagonale = diagonal(layer,(x,y))
    diagonale_t = diagonal_t(layer,(x,y))
    victory = row(horizontale,long) or row(verticale,long) or row(diagonale,long) or row(diagonale_t,long)
    return victory

 # def row_layer(layer,n,coord): #returns if there is a horizontal, vertical, or diagonal row of n '1' with the point whose coordinates are (x,y) in the layer, coord is a tuple
 #     x,y = coord[0], coord[1]
 #     long = len(layer)
 #     horizontal = layer[x]
 #     vertical = np.transpose(layer)[y]
 #     diagonal_d = np.diag(layer,y-x)
 #     diagonal_g = np.diag(np.fliplr(layer),(long-y)-x)
 #     victory = row(horizontal,n) or row(vertical,n) or row(diagonal_d,n) or row(diagonal_g,n)
 #      return victory


def diagonal(tab,coord): #returns the diagonal of the table if the element is on the diagonal , coord is a tuple
    diagonale = []
    if coord[0] == coord[1]:
        for i,j in enumerate(tab):
            diagonale.append(j[i])
    return diagonale

def diagonal_t(tab,coord): #returns the other diagonal of the table(which is a square) if the element is on this diagonal , coord is a tuple
    diagonale = []
    n = len(tab)
    if coord[0] == n-1 - coord[1]:
        for i, j in enumerate(tab):
            diagonale.append(j[n-1-i])
    return diagonale

def vertical(tab,coord): #returns the column where the element is of the table
    verticale = []
    for i in tab:
        verticale.append(i[coord[1]])
    return verticale






# jeu = Game(4)
# print(jeu.bag)
# print(jeu.board)
# jeu.select_piece(3)
# print(jeu.selected_piece)
# print(jeu.bag)
# jeu.play_piece((1,1))
# print(jeu.board)
# jeu.select_piece(3)
# jeu.select_piece(4)
# print(jeu.selected_piece)
# jeu.play_piece((1,1))
# print(jeu.board)
