class Piece:
    def __init__(self, charact):
        self.charact = charact
        self.size = len(charact)
        self.coord = ()

        # TODO : rajouter un attribut self.num qui représente la valeur décimal des charactéristiques de la plèce
        # TODO : OU inversement

    def __repr__(self):
        return str(self.charact)

def to_bin(p):
    return

def to_decimal(p):
    return

def from_bin(binary_number):
    pass

def from_decimal(decimal_number, size):
    charact = []
    # transforms the number in a binary number, adding '0' to have the same length for all numbers
    for j in str(format(decimal_number, 'b')).rjust(size, '0'):
        charact.append(int(j))  # creates a list composed by the numbers of the binary number
    return Piece(charact)
