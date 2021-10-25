import random as r
import test
import time

from main import *
from hands import *

#tuple t = (1, 3, "c")
#set s = {"a", "b"}
#object = {}
#list = ["a", "b"]
#dict = {"a":1, "b": 2}

#deck
deck = [*range(52)]
deckr = r.sample(range(52),52)
cards = HandToCardTuple(deckr)
print("randomdeck", cards)

rhand = r.sample(range(52), 13)
print("randomhand", rhand)

print("suit", deck[0]%4, deck[1]%4, deck[2]%4, deck[3]%4, card(deck[0]))
print("number", deck[16]/4, int(deck[17]/4))

def checkpair(hand, expected):
    r = pair(hand)
    assert r == expected

def checktriple(hand, expected):
    r = triple(hand)
    assert r == expected

def checkflush(hand, expected):
    r = flush(hand)
    assert r == expected

def checkstraight(hand, expected):
    t0 = time.perf_counter()
    h2 = hand.copy()
    h2.sort()
    for x in h2:
        x = number(x)
        print(x)
    r = straight(hand)
    t1 = time.perf_counter()
    d = t1-t0
    print("Time:", d)
    assert r == expected

#checkstraight(handws2, True)


#-- Tests
def test_pair_falsej():
    checkpair(handj1, False)

def test_pair_false1():
    checkpair(handldf, False)

def test_pair_false2():
    checkpair(hands1, False)

def test_pair_true1():
    checkpair(hand2d3d4d5d5s, True)

def test_triple_falsej():
    checktriple(handj1, False)

def test_triple_false1():
    checktriple(hand2d3d4d5d5s, False)

def test_triple_false2():
    sh = hand2d3d4d5d5s.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    print(st)
    r = XOfAKindTuple(st)
    print (r)
    assert r == False

def test_triple_true1():
    checktriple(handt1, True)

def test_triple_true2():
    sh = handt1.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    print(st)
    r = XOfAKindTuple(st)
    print (r)
    assert r

def test_flush_falsej():
    checkflush(handj1, False)

def test_flush_false():
    checkflush(hand2d3d4d5d5s, False)

def test_flush_true():
    checkflush(handldf, True)

def test_flush_false2():
    sh = hand2d3d4d5d5s.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    print(st)
    r = flushTuple(st)
    print (r)
    assert r == False

def test_flush_true2():
    sh = handldf.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    print(st)
    r = flushTuple(st)
    print (r)
    assert r

def test_straight_falsej():
    checkstraight(handj1, False)

def test_straight_false1():
    checkstraight(hand2d3d4d5d5s, False)

def test_straight_true1():
    checkstraight(handldf, True)

def test_straight_true2():
    checkstraight(hands1, True)

def test_straight_wrapped_true():
    checkstraight(handws, True)

def test_straight_wrapped_true2():
    checkstraight(handws2, False)

def test_straight_wrapped_true3():
    checkstraight(handws3, True)

def test_straight_wrapped_true4():
    t0 = time.perf_counter()
    sh = handws3.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    r = straightTuple(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:", st)
    print ("Result:", r)
    print("Time:", d)
    assert r == True

def test_straight_wrapped_false5():
    t0 = time.perf_counter()
    sh = handj1.copy()
    sh.sort()
    st = HandToCardTuple(sh)
    r = straightTuple(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:", st)
    print ("Result:", r)
    print("Time:", d)
    assert r == False


test_straight_wrapped_true3()
test_straight_wrapped_true4()
test_straight_falsej()
test_straight_wrapped_false5()