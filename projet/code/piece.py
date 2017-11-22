class Piece:  # cette classe définit ce qu'est une pièce du jeu

    def __init__(self, color, height, shape, matter):
        self.color = color  # couleur : clair/foncé (o/1 par exemple)
        self.height = height  # hauteur : gtand/petit (0/1 par ex)
        self.shape = shape  # rond/carré (0/1 par ex )
        self.matter = matter  # creux ou plein (idem)

