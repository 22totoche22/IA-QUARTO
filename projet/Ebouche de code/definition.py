class Piece: # cette classe définit ce qu'est une pièce du jeu
    
    def __init__(self, color, height, shape, matter):
        self.color = color # couleur : clair/foncé (o/1 par exemple)
        self.height = height # hauteur : gtand/petit (0/1 par ex)
        self.shape = shape # rond/carré (0/1 par ex )
        self.matter = matter # creux ou plein (idem)
        
class Game(Piece): # cette classe définit ce qu'est une situation de jeux (un étape, une configuration du plateau à un moment donné ...)
    
    def __init__(self):
        self.set = [[],[],[],[]] # ceci est le plateau du jeu 4*4 avec aucune pièce dessus (ne fonctionne pas commen ça mais vous comprenez l'idée)
        self.bag = {}# les pièces qui sont sur le côté du jeu donc pas sur le plateau (dans un sac en fait). Chaque pièce étant unique, on attribue à achacune un idéntifiant id, d'où l'idée d'un dictionnaire où les clés sont les identifiants.
        
    def add(self, id_piece, coord): # méthode qui ajoute une pièce reconnue par son identifiant sur le plateau à la case de coordonée coord ( couple)
        self.set[coord[0]][coord[1]] = self.bag[id_piece]
        del self.bag[id_piece] # on enlève la pièce du sac car elle est sur le plateau
        
        