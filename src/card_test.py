import random as r
import test
import time

from main import *
from hands import *
from Card import *

#tuple t = (1, 3, "c")
#set s = {"a", "b"}
#object = {}
#list = ["a", "b"]
#dict = {"a":1, "b": 2}

#deck

c = Card(39)
print(c.value, c.number, c.suit)
print(c.name()) # Q-S

def test_cardname():
    c = Card(38)
    assert c.name() == "Q-H"

#def a(f, c):
 #   f(c)

#c = Card(38)
#a(test_cardname, c)

def createTupleHand(hand):
    hand.sort()
    return ValuesToCards(hand)


def Check(f, hand, expected):
    print("Testing: ", f.__name__)
    t0 = time.perf_counter()
    st = createTupleHand(hand)
    r = f(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:{0}, Time:{1}\nResult:{2}".format(st, d, r))
    assert r == expected

def test_triple_false2():
    Check(XOfAKindTuple, hand2d3d4d5d5s, -1)

def test_triple_true2():
    Check(XOfAKindTuple,handt1, 8)

def test_flushTuple_false():
    Check(FlushTuple, hand2d3d4d5d5s, False)

def test_flushTuple_true():
    Check(FlushTuple, handldf, True)

def test_straight_wrapped_1_true():
    Check(StraightTuple, handws3, True)

def test_straight_wrapped_2_false():
    Check(StraightTuple, handj1, False)

def test_straightflushTuple_true():
    Check(StraightFlushTuple, handldf, True)

def test_straightflushTuple_false():
    Check(StraightFlushTuple, handws, False)

def test_fullHouse_true():
    Check(FullHouse, handfh, 1)

def test_fullHouse_true2():
    Check(FullHouse, handws3, 0)

def test_fullHouse_false():
    Check(FullHouse, handws, -1)

test_straight_wrapped_1_true()
test_straight_wrapped_2_false()
test_fullHouse_true()