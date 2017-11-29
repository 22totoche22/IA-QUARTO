#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
import piece



PLAYER_A = 1
PLAYER_B = 0
SIZE = 4


class Bag_error(Exception):
    pass

class Cell_error(Exception):
    pass
        
class Game:

    def __init__(self, size):
        self.size = size
        self.board = [[[None for i in range(self.size)] for j in range(self.size)] for k in range(self.size)] #creates a 3D board

        self.bag = {}
        self.init_full_bag()

        self.player = PLAYER_A
        self.selected_piece = None
        self.win = False
        self.end = False
        self.coords = [(i,j) for i in range(self.size) for j in range(self.size)] #list of all possibles coordinates


    def init_full_bag(self):   #initializes the bag at the beginning of the game
        for i in range(2**self.size):
            self.bag[i] = piece.Piece(i,self.size)                  #adds the list in the bag, the key equals to the binary number


    def play_piece(self,coord):
        x, y = coord[0], coord[1]
        try :
            coord = self.coords[self.coords.index(coord)]
            del self.coords[self.coords.index(coord)]
        except Exception:  # Error if the coordinates "coord" have already been choosen
                print(Cell_error("this cell is already taken: Choose an other one"))
                x = int(input("x coord = "))
                y = int(input("y coord = "))
                self.play_piece((x,y))

        for k in range(self.size):
                self.board[x][y][k] = self.selected_piece.charact[k]

    def select_piece(self,num):
        try:
            piece = self.bag[num]
            del self.bag[num]                             #removes the Piece from the bag
            self.selected_piece = piece
        except Exception: #Error if self.bag[num_piece] doesn't exist anymore
            print(Bag_error("this piece has already been played: Choose an other one"))
            i = int(input("Numéro de la pièce = "))
            self.select_piece(i)


    def full_row(self,coord,n): #verifies if there is a full horizontal, vertical, or diagonal row of n pieces with the same characteristics after putting the piece at the coordinates(x,y) on the board
        victory = []
        for i in range(self.size):
            layer_i = layer_tab(self.board,i)
            victory.append(row_layer(layer_i,n,coord))
        return True in victory

    def __repr__(self):
        """
        Renvoi un affichage de l'état de jeu courant
        :return: (String) res : représente l'état de jeu
        """
        res = ""
        res += "Pièce sélectionnée par le joueur adverse : " + str(self.selected_piece) + "\n"*2

        for i_layer in range(self.size):
            # We go through all the layers
            for y_board in range(self.size):
                for x_board in range(self.size):
                    res += "." if self.board[x_board][y_board][i_layer] is None else str(self.board[x_board][y_board][i_layer])
                res += "\n"
            res += "\n"*2
        return res







def row(list,n): #returns if there is a row of n '1' in a simple list
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


def layer_tab(board, k):     #return the k layer of a 3D board
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
