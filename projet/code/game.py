import numpy as np

PLAYER_A = 1
PLAYER_B = 0

class Game:

    def __init__(self, n):
        self.set = [[None for i in range(n)] for j in range(n)]
        self.bag = {}
        self.player = PLAYER_A
        self.win = False
        self.end = False
        self.winner = None

    def __repr__(self):
        layer = [np.zeros((n ,n) ) *n]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    layer[k][i][j] = self.set[i][j].descr[k]
        for k in range(n):
            print("caractéristique  " ,k, " : ")
            print(layer[k])



   
    
         
        

