
from Card import *


def ValuesToCards(hand):
    cards = []
    for v in hand:
        c = Card(v)
        cards.append(c)
    return cards

def XOfAKindTuple(cards, x=3, notEqualTo=-1):
    n1 = -1
    count = 0
    for c in cards: #0-3
        n2 = c.number
        if n2 > n1 or n2 == notEqualTo:
            count = 1
            n1 = n2
        else:
            count = count +1
        if count == x:
            return n2
    return -1

def FullHouse(cards):
    t = XOfAKindTuple(cards, 3)
    p = XOfAKindTuple(cards, 2, t)
    if t>-1 and p>-1 and t!=p:
        return t
    return -1

def FlushTuple(cards, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in cards:
            if c.suit == s:
                count = count +1
            if count == x:
                return True
    return False


def StraightTuple(cards, x=5):
    count = 1
    countLow = -1
    n1 = cards[0].number # number value 0-12
    s1 = cards[0].suit # suit value 0-3
    indexArray = [*range(1,len(cards))] # range 1-13 = 1-12! (stop is exclusive)
    first = n1
    for i in indexArray: # 0-3, 0-11
        n2=cards[i].number # 1-4, 1-12
        s2=cards[i].suit
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


def StraightFlushTuple(cards, x=5):
    count = 1
    countLow = -1
    n1 = cards[0].number # number value 0-12
    s1 = cards[0].suit # suit value 0-3
    indexArray = [*range(1,len(cards))] # range 1-13 = 1-12! (stop is exclusive)
    first = n1
    for i in indexArray: # 0-3, 0-11
        n2=cards[i].number # 1-4, 1-12
        s2=cards[i].suit # 0-3
        diff = n2-n1
        #print("{0}, {1}, {2}".format(c1,c2, diff))
        if diff == 1 and s1==s2:
            count = count+1
        elif diff == -12 and s1==s2: # allow for wrap around straights (e.g. KA234) 
            count = count +1
        elif diff > 1:
            if first == 0: # did we start at 3?
                if countLow == -1:
                    countLow = count
            count = 1
        if count == x:
            return True
        n1 = n2
        s1 = s2
    #print("no straight in ", h2)
    if n2 == 12:
        if count + countLow == x:
            return True
    return False
