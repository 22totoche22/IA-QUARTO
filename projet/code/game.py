#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np

PLAYER_A = 1
PLAYER_B = 0
SIZE = 4


class Bag_error(Exception):
    pass

class Cell_error(Exception):
    pass

class Piece:
     
    def __init__(self, charact):
         self.charact = charact
         self.coord = ()
         
    def __repr__(self):
        return str(self.charact)
        
class Game:
    
    def __init__(self, size):
        self.size = size
        self.board = [[[None for i in range(self.size)] for j in range(self.size)] for k in range(self.size)] #creates a 3D board
        self.bag = {}
        self.player = PLAYER_A
        self.win = False
        self.end = False
        self.coords = [(i,j) for i in range(self.size) for j in range(self.size)] #list of all possibles coordinates


    def full_bag(self):   #initializes the bag at the beginning of the game
        for i in range(2**self.size):
            size_uplet = []
            for j in str(format(i,'b')).rjust(self.size,'0'):   #transforms the number in a binary number, adding '0' to have the same length for all numbers
                size_uplet.append(int(j))                       #creates a list composed by the numbers of the binary number
            self.bag[i] = Piece(size_uplet)                     #adds the list in the bag, the key equals to the binary number


    def play_piece(self,num_piece,coord): #adds a object Piece from the bag  on the board at the coordinates (x,y) and remove it from the bag, coord is a tuple
        x,y = coord[0], coord[1]

        for k in range(self.size):
            try:
                self.board[x][y][k] = self.bag[num_piece].charact[k]
            except Exception: #Error if self.bag[num_piece] doesn't exist anymore
                print(Bag_error("this piece as already been played: Choose an other one"))
                num_piece = int(input("num_piece?"))
                self.board[x][y][k] = self.bag[num_piece].charact[k] #adds the Piece on the board

            try:
                coord = self.coords[self.coords.index(coord)]
            except Exception: #Error if the coordinates "coord" have already been choosen 
                print(Cell_error("this cell is already taken: Choose an other ones"))
                coord = tuple(input("coord?"))
                self.board[x][y][k] = self.bag[num_piece].charact[k] #adds the Piece on the board

        
        del self.coords[self.coords.index(coord)]
        del self.bag[num_piece]                             #removes the Piece from the bag
            

#rajouter erreur si pièce plus dans le sac,...


    def full_row(self,coord,n): #verifies if there is a full horizontal, vertical, or diagonal row of n pieces with the same characteristics after putting the piece at the coordinates(x,y) on the board
        victory = []
        for i in range(self.size):
            layer_i = layer_tab(self.board,i)
            victory.append(row_layer(layer_i,n,coord))
        return True in victory


def layer_tab(board, k):     #return the k layer of a 3D board
    n = len(board)
    if k < n:
        layer = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                    layer[i][j] = board[i][j][k]
        return np.array(layer)


def row(list,n): #returns if there is a row of n '1' in a simple list
    compteur = 0
    max_compteur = 0
    for i in list:
        if i == 1:
            compteur += 1
            max_compteur = max(compteur,max_compteur)
        else:
            compteur = 0
    return max_compteur == n


def row_layer(layer,n,coord): #returns if there is a horizontal, vertical, or diagonal row of n '1' with the point whose coordinates are (x,y) in the layer, coord is a tuple
    x,y = coord[0], coord[1]
    long = len(layer)
    horizontal = layer[x]
    vertical = np.transpose(layer)[y]
    diagonal_d = np.diag(layer,y-x)
    diagonal_g = np.diag(np.fliplr(layer),(long-y)-x)
    victory = row(horizontal,n) or row(vertical,n) or row(diagonal_d,n) or row(diagonal_g,n)
    return victory


    
piece = Piece([0,1,1,0])
jeu = Game(SIZE)
jeu.full_bag()



jeu.play_piece(2,(2,3))
jeu.play_piece(2,(1,3))
print(jeu.board)
print(jeu.bag)
print(jeu.coords)
































