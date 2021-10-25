import random
from main import *

# Card Values
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

# sample 5 card hands
handldf = [0,4,8,12,16] # 3d, 4d, 5d, 6d, 7d
hand2d3d4d5d5s = [0,4,8,12,15] # 3d, 4d, 5d, 6d, 6s
hands1 = [38,33,31,24,22] # run 8h,9d, 10s,jc,qh
handt1 = [34,32,44,1,33] # triple jh,jd,ad,3c,jc
handj1 = [4,8,12,37,41,45,49, 22,26,30] # junk 4,5,6,K,A,2, 8,9,10,J
handws = [40,44,49,2,7] # wrapped straight KD,AD,2C,3H,4S
handws2 = [47,48,49,50,51,0,1,2,3,4]
handws3 = [47,48,49,50,51,0,1,2,3,4,8]

# all suits in deck
deck = [*range(52)]

#suits
clubs = [*range(0, 52, 4)]
diamonds = [*range(1,52, 4)]
hearts = [*range(2,52, 4)]
spades = [*range(3,52, 4)]

deckr = random.sample(range(52),52)
cards = HandToCardTuple(deckr)
#print("randomdeck", cards)

rhand = random.sample(range(52), 13)
#print("randomhand", rhand)
