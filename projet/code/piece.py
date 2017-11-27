class Piece:
    def __init__(self, num, size):
        self.num = num
        self.size = size
        self.charact = from_decimal(self.num,self.size)
        self.coord = ()

    def __repr__(self):
        return str(self.charact)

# def to_bin(p):
#     return
#
# def to_decimal(p):
#     return
#
# def from_bin(binary_number):
#     pass

def from_decimal(decimal_number, size):
    charact = []
    # transforms the number in a binary number, adding '0' to have the same length for all numbers
    for j in str(format(decimal_number, 'b')).rjust(size, '0'):
        charact.append(int(j))  # creates a list composed by the numbers of the binary number
    return charact

