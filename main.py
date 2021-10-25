
# add pytest

def BigTwoSuitValue(x):
    return x%4

def BigTwoSuitString(x):
    s = BigTwoSuitValue(x)
    if s == 0:
         ss = "D"
    elif s == 1:
        ss = "C"
    elif s == 2:
        ss = "H"
    elif s == 3:
        ss = "S"
    return ss

def number(x):
    return BigTwoNumberValue(x)

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
def BigTwoNumberString(x):
    if x<32:
        return str(int(x/4)+3)
    if x<36:
        return "J"
    if x<40:
        return "Q"
    if x<44:
        return "K"
    if x<48:
        return "A"
    if x< 52:
        return "2"
    return ""

def BigTwoNumberValue(x):
    return int(x/4)

def BigTwoCardTuple(x):
    numberValue= BigTwoNumberValue(x)
    numberString = BigTwoNumberString(x)
    suitValue = BigTwoSuitValue(x)
    suitString=BigTwoSuitString(x)
    return (x, numberValue, numberString, suitValue, suitString)

def card(x): 
    t = BigTwoCardTuple(x)
    return "{0}-{1}".format(t[2], t[4])

def pair(hand):
    for i in range(len(hand)-1): #0-3
        first = hand[i]
        for j in range(len(hand)-i-1): #0-3, 0-2, 0-1, 0
            second = hand[j+i+1]
            if number(first) == number(second):
                return True
    return False

def triple(hand):
    for i in range(len(hand)-1): #0-3
        first = hand[i]
        for j in range(len(hand)-i-1): #0-3, 0-2, 0-1, 0
            second = hand[j+i+1]
            for k in range(len(hand)-i-j-2): #0-2, 0-1, 0
                third = hand[k+j+i+2]
                if number(first) == number(second) == number(third):
                    return True
    return False

def flush(hand, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in hand:
            if BigTwoSuitValue(c) == s:
                count = count +1
            if count == x:
                return True
    return False

def straight(hand, x=5):
    h2 = hand.copy()
    h2.sort()
    count = 0
    countLow = -1
    fc = h2[0]
    indexArray = [*range(1,len(h2))]
    c1=number(fc)
    first = c1
    for c in indexArray: # 0-3, 0-11
        c2=number(h2[c]) # 1-4, 1-12
        diff = c2-c1
        #print("{0}, {1}, {2}".format(c1,c2, diff))
        if diff == 1:
            count = count+1
        elif diff == -12: # allow for wrap around straights (e.g. KA234) 
            count = count +1
        elif diff > 1:
            if first == 0:
                if countLow == -1:
                    countLow = count
            count = 0
        if count == x-1:
            return True
        c1 = c2
    #print("no straight in ", h2)
    if c2 == 12:
        if count + countLow == x-2:
            return True
    return False

