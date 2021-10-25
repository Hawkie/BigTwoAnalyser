
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

#Tuple
#0 value 0-51
#1 number 0-12
#2 nstr 3-10,J,Q,K,A,2
#3 suit 0-3
#4 suitStr D,C,H,S
def BigTwoCardTuple(x):
    numberValue= BigTwoNumberValue(x)
    numberString = BigTwoNumberString(x)
    suitValue = BigTwoSuitValue(x)
    suitString=BigTwoSuitString(x)
    return (x, numberValue, numberString, suitValue, suitString)

def CardString(x): 
    t = BigTwoCardTuple(x)
    return "{0}-{1}".format(t[2], t[4])

def HandToCardTuple(hand):
    cards = []
    for c in hand:
        x = BigTwoCardTuple(c)
        cards.append(x)
    return cards

def XOfAKindTuple(sortedTuple, x=3):
    n1 = -1
    count = 0
    for c in sortedTuple: #0-3
        n2 = c[1]
        if (n1 != n2):
            count = 1
            n1 = n2
        else:
            count = count +1
        if count == x:
            return True
    return False

def flushTuple(sortedTupleList, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in sortedTupleList:
            if c[3] == s:
                count = count +1
            if count == x:
                return True
    return False


def straightTuple(sortedTupleList, x=5):
    count = 1
    countLow = -1
    n1 = sortedTupleList[0][1]
    indexArray = [*range(1,len(sortedTupleList))] # range 1-13 = 1-12! (stop is exclusive)
    first = n1
    for i in indexArray: # 0-3, 0-11
        n2=sortedTupleList[i][1] # 1-4, 1-12
        diff = n2-n1
        #print("{0}, {1}, {2}".format(c1,c2, diff))
        if diff == 1:
            count = count+1
        elif diff == -12: # allow for wrap around straights (e.g. KA234) 
            count = count +1
        elif diff > 1:
            if first == 0: # did we start at 3?
                if countLow == -1:
                    countLow = count
            count = 1
        if count == x:
            return True
        n1 = n2
    #print("no straight in ", h2)
    if n2 == 12:
        if count + countLow == x:
            return True
    return False

