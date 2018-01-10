class Piece:

    def __init__(self, num, size):
        """
        A piece is a decimal number num from 0 to size whom binary representation (attribute : charact) represents the
        characteristics (one digit 0 or 1 for the value of a characteristic). coord is the couple of the position of the
        piece on the board.
        :param num: int
        :param size: int
        """
        self.num = num
        self.size = size
        self.charact = from_decimal(self.num, self.size)
        self.coord = ()

    def __repr__(self):
        param = "{: >" + str(self.size+4) + "}"
        s = "{} : " + param
        return s.format(to_decimal(self.charact), str(self.charact))


def from_decimal(decimal_number, size):
    """
    Transforms the number decimal_number in a binary number, adding '0' to have the same length size for all numbers.
    Return a list composed by the numbers of the binary number
    :param decimal_number: int
    :param size: int
    :return: list
    """
    charact = []
    for j in str(format(decimal_number, 'b')).rjust(size, '0'):
        charact.append(int(j))
    return charact


def to_bin(charact):
    """
    Shows the binary equivalent to the piece characteristics
    Example : [0,1,0,1,1] ==> 0b1011
    For example
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
    for i, c in enumerate(reversed(charact)):
        res += c * 2**i
    return res
