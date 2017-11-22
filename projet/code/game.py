class Game: # cette classe définit ce qu'est une situation de jeux (un étape, une configuration du plateau à un moment donné ...)

    def __init__(self):
        self.board = [[], [], [],
                    []]  # ceci est le plateau du jeu 4*4 avec aucune pièce dessus (ne fonctionne pas commen ça mais vous comprenez l'idée)
        self.bag = {}  # les pièces qui sont sur le côté du jeu donc pas sur le plateau (dans un sac en fait). Chaque pièce étant unique, on attribue à achacune un idéntifiant id, d'où l'idée d'un dictionnaire où les clés sont les identifiants.

    def add(self, id_piece,
            coord):  # méthode qui ajoute une pièce reconnue par son identifiant sur le plateau à la case de coordonée coord ( couple)
        self.set[coord[0]][coord[1]] = self.bag[id_piece]
        del self.bag[id_piece]  # on enlève la pièce du sac car elle est sur le plateau
        






### test         

import numpy as np

        
class Piece:
     
    def __init__(self, descr):
         self.descr = descr
         
    def __repr__(self):
        print(self.descr)
        
class Game(Piece):
    
    def __init__(self, n):
        self.set = np.zeros((n,n))
        self.bag = {}
        self.player = "PLAYER A"
        self.win = False
        self.end = False
        self.winner = None
    
    def __repr__(self):
        layer = [np.zeros((n,n))*n]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    layer[k][i][j] = self.set[i][j].descr[k] 
        for k in range(n):
            print("caractéristique  ",k, " : ")
            print(layer[k])
   
    
         
        

