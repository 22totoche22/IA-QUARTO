
import numpy as np

PLAYER_A = 1
PLAYER_B = 0
SIZE = 4

class Piece:
     
    def __init__(self, charact):
         self.charact = charact
         
    def __repr__(self):
        return str(self.charact)
        
class Game:
    
    def __init__(self, size):
        self.size = size
        self.board = [[None for i in range(self.size)] for j in range(self.size)]
        self.bag = {}
        self.player = PLAYER_A
        self.win = False
        self.end = False

# __repr__ doit renvoyer un string

    # def __repr__(self):
    #     layer = [np.zeros((self.size ,self.size) ) *self.size]
    #     print(layer)
    #     for i in range(self.size-1):
    #         for j in range(self.size-1):
    #             for k in range(self.size-1):
    #                 print (i,j,k)
    #                 layer[i][j][k] = self.set[i][j].charact[k]
    #     for k in range(self.size):
    #         print("caractéristique  " ,k, " : ")
    #         print(layer[k])


    def full_bag(self):   #initializes the bag at the beginning of the game
        for i in range(2**self.size):
            size_uplet = []
            for j in str(format(i,'b')).rjust(self.size,'0'):   #transforms the number in a binary number, adding '0' to have the same length for all numbers
                size_uplet.append(int(j))                       #creates a list composed by the numbers of the binary number
            self.bag[i] = Piece(size_uplet)                     #adds the list in the bag, the key equals to the binary number

    def play_piece(self,num_piece,coord): #adds a object Piece from the bag  on the board at the coordinates (x,y) and remove it from the bag, coord is a tuple
        x,y = coord[0], coord[1]
        if self.board[x][y] == None:
            self.board[x][y] = self.bag[num_piece]              #adds the Piece on the board
            del self.bag[num_piece]                             #removes the Piece from the bag

#rajouter erreur si pièce plus dans le sac,...

    def full_row(self): #verifies if there is a full horizontal, vertical, or diagonal row of n pieces which have a common characteristic
        pass



a = Game(SIZE)
print(a.bag)
a.full_bag()
print(a.bag)
print(a.board)
a.play_piece(1,(0,0))
print(a.board)
print(a.bag)





