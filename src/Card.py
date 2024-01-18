# Big Two Card Values
#	d	c	h	s
#3	0	1	2	3
#4	4	5	6	7
#5	8	9	10	11
#6	12	13	14	15
#7	16	17	18	19
#8	20	21	22	23
#9	24	25	26	27
#10	28	29	30	31
#j	32	33	34	35
#q	36	37	38	39
#k	40	41	42	43
#a	44	45	46	47
#2	48	49	50	51

class Card(object):
    def __init__(self, value):
        self._v = value
        self._n = int(value/4)
        self._s = value%4

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self._v == other._v

    @property
    def value(self):
        return self._v

    @property
    def number(self):
        return self._n

    def number_name(self):
        if self._v<28:
            return str(int(self._v/4)+3)
        if self._v<32:
            return "T"
        if self._v<36:
            return "J"
        if self._v<40:
            return "Q"
        if self._v<44:
            return "K"
        if self._v<48:
            return "A"
        if self._v< 52:
            return "2"
        return "" 

    @property
    def suit(self):
        return self._s

    def suit_name(self):
        if self.suit == 0:
            sn = "D"
        elif self.suit == 1:
            sn = "C"
        elif self.suit == 2:
            sn = "H"
        elif self.suit == 3:
            sn = "S"
        return sn

    @property
    def name(self):
        return "{0}-{1}".format(self.number_name(), self.suit_name())
