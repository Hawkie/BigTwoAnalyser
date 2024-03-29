import random
from main import *

# Card Values
# 	d	c	h	s
# 3	0	1	2	3
# 4	4	5	6	7
# 5	8	9	10	11
# 6	12	13	14	15
# 7	16	17	18	19
# 8	20	21	22	23
# 9	24	25	26	27
# 10	28	29	30	31
# j	32	33	34	35
# q	36	37	38	39
# k	40	41	42	43
# a	44	45	46	47
# 2	48	49	50	51

# sample 5 card hands
handldf = [0, 4, 8, 12, 16]  # 3d, 4d, 5d, 6d, 7d
handldfmixedup = [
    0,
    3,
    4,
    7,
    34,
    11,
    35,
    12,
    15,
    36,
    16,
    19,
]  # 3=3s, 7=4s, 11=5s, 15=6s, 19=7s
hand2d3d4d5d5s = [0, 4, 8, 12, 15]  # 3d, 4d, 5d, 6d, 6s
hands1 = [38, 33, 31, 24, 22]  # straight 8h,9d, 10s,jc,qh
handt1 = [34, 32, 44, 1, 33]  # triple jh,jd,ad,3c,jc
handj1 = [4, 8, 12, 37, 41, 45, 49, 22, 26, 30]  # junk 4,5,6,K,A,2, 8,9,10,J
handws = [40, 44, 49, 2, 7]  # wrapped straight KD,AD,2C,3H,4S
handnws2 = [
    47,
    48,
    49,
    50,
    51,
    0,
    1,
    2,
    3,
    4,
]  # A222233334 (only 4 card straight and full house)
handws3 = [
    47,
    48,
    49,
    50,
    51,
    0,
    1,
    2,
    3,
    4,
    8,
]  # A2222333345 (5 card straight and full house)
handfh = [4, 5, 6, 8, 9]  # 44455 (full house)

# all suits in deck
deck = [*range(52)]
hand1 = deck[:13]
hand2 = deck[13:26]
hand3 = deck[26:39]
hand4 = deck[39:52]

# suits
clubs = [*range(0, 52, 4)]
diamonds = [*range(1, 52, 4)]
hearts = [*range(2, 52, 4)]
spades = [*range(3, 52, 4)]

deckr = random.sample(range(52), 52)
cards = values_to_cards(deckr)

rhand = random.sample(range(52), 13)
# print("randomhand", rhand)
