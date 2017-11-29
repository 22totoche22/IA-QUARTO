class Piece:
    def __init__(self, num, size):
        self.num = num
        self.size = size
        self.charact = from_decimal(self.num,self.size)
        self.coord = ()

    def __repr__(self):
        # TODO : enhance this param
        param = "{: >"+str(self.size+4)+"}"
        s = "{} : "+param
        return s.format(to_decimal(self.charact), str(self.charact))


def from_decimal(decimal_number, size):
    charact = []
    # transforms the number in a binary number, adding '0' to have the same length for all numbers
    for j in str(format(decimal_number, 'b')).rjust(size, '0'):
        charact.append(int(j))  # creates a list composed by the numbers of the binary number
    return charact


def to_bin(charact):
    """
    Shows the binary equivalent to the piece characteristics
    Example : [0,1,0,1,1] ==> 0b1011
    Par exemple
    :param charact:
    :return: b : the binary representation of the piece
    """
    return bin(to_decimal(charact))

def to_decimal(charact):
    """
    Shows the deximal equivalent to the piece characteristics
    Example : [0,1,0,1,1] ==> 11
    Par exemple
    :param charact: list of the piece's caracteristics
    :return: res : decimal representative
    """
    res = 0
    size = len(charact)
    for (i, c) in enumerate(reversed(charact)):
        res += c * 2**(i)
    return res

