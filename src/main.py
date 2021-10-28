
from Card import *

def ValuesToCards(hand):
    cards = []
    for v in hand:
        c = Card(v)
        cards.append(c)
    return cards

def IsXOfAKindTuple(cards, x=3, notEqualTo=-1):
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
            return c
    return None

def IsFullHouse(cards):
    t = IsXOfAKindTuple(cards, 3)
    if t is not None:
        p = IsXOfAKindTuple(cards, 2, t.number)
        if p is not None:
            if t!=p:
                return t
    return None

def IsFlush(cards, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in cards:
            if c.suit == s:
                count = count +1
            if count == x:
                return c
    return None

def NumberDiffPred(c1,c2):
    diff = c2.number-c1.number
    if diff == 1 or diff == -12:
        return 1
    elif diff > 1:
        return -1
    return 0 # if diff = 0
    

def NumberDiffAndSuitEqualPred(c1,c2):
    diff = c2.number-c1.number
    if c2.suit == c1.suit:
        if diff == 1 or diff == -12:
            return 1
    return -1

def IsStraight(cards, x=5, pred=lambda *c: NumberDiffPred(c[0], c[1])):
    count = 1
    countLow = 0
    c1 = cards[0]
    first = c1
    for c in cards[1:]: # 0-3, 0-11
        p = pred(c1, c)
        if p == 1:
            count += 1
        elif p == -1:
            if first.number == 0: # wrap function -> did we start at 3?
                if countLow == 0:
                    countLow = count
            count = 1
        if count == x:
            return c
        c1 = c
    if c1.number == 12: # n = 0-12 (12 = 2)
        if count + countLow == x:
            return c1
    return None

def IsStraightFlush(cards, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        suitedCards = []
        for c in cards:
            if c.suit == s:
                suitedCards.append(c)
        if len(suitedCards) > 1:
            r = IsStraight(suitedCards)
            if r is not None:
                return r
    return None

