class Piece:
    
    def __init__(self, color, height, shape, matter):
        self.color = color
        self.height = height
        self.shape = shape
        self.matter = matter
        
class Game(Piece):
    
    def __init__(self):
        self.set = [[None, None,None][None, None,None],[None, None,None]]
        self.bag = {}
        
    def add(self, id_piece, coord):
        self.set[coord[0]][coord[1]] = self.bag[id_piece]
        del self.bag[id_piece]
        
        