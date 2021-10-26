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




def createTupleHand(hand):
    sh = hand.copy()
    sh.sort()
    return HandToCardTuple(sh)

def checkflushTuple(hand, expected):
    t0 = time.perf_counter()
    st = createTupleHand(hand)
    r = FlushTuple(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:", st)
    print ("Result:", r)
    print("Time:", d)
    assert r == expected



def checkstraightTuple_wrapped(hand, expected):
    t0 = time.perf_counter()
    st = createTupleHand(hand)
    r = StraightTuple(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:", st)
    print ("Result:", r)
    print("Time:", d)
    assert r == expected

def CheckStraightFlushTuple_wrapped(hand, expected):
    t0 = time.perf_counter()
    st = createTupleHand(hand)
    r = StraightFlushTuple(st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:", st)
    print ("Result:", r)
    print("Time:", d)
    assert r == expected

def test_triple_false2():
    st = createTupleHand(hand2d3d4d5d5s)
    print(st)
    r = XOfAKindTuple(st)
    print (r)
    assert r == False


def test_triple_true2():
    st = createTupleHand(handt1)
    print(st)
    r = XOfAKindTuple(st)
    print (r)
    assert r


def test_flushTuple_false():
    checkflushTuple(hand2d3d4d5d5s, False)

def test_flushTuple_true():
    checkflushTuple(handldf, True)

def test_straight_wrapped_1_true():
    checkstraightTuple_wrapped(handws3, True)

def test_straight_wrapped_2_false():
    checkstraightTuple_wrapped(handj1, False)

def test_straightflushTuple_true():
    CheckStraightFlushTuple_wrapped(handldf, True)

def test_straightflushTuple_false():
    CheckStraightFlushTuple_wrapped(handws, False)

test_straight_wrapped_1_true()
test_straight_wrapped_2_false()