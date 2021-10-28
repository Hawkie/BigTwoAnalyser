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
print("Testing Card Props for QS",c.name,c.value, c.number, c.suit)

def test_cardname():
    c = Card(38)
    assert c.name == "Q-H"

#def a(f, c):
 #   f(c)

#c = Card(38)
#a(test_cardname, c)

def createTupleHand(hand):
    hand.sort()
    return ValuesToCards(hand)

def Execute(f, hand):
    return f(hand)

def Check(f, hand, expected):
    print("Testing: ", f.__name__)
    t0 = time.perf_counter()
    st = createTupleHand(hand)
    r = Execute(f, st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:{0}, Time:{1}\nResult:{2}".format(st, d, r))
    assert r == expected

def test_triple_false2():
    Check(IsXOfAKindTuple, hand2d3d4d5d5s, None)

def test_triple_true2():
    Check(IsXOfAKindTuple,handt1, Card(34)) # JH

def test_flushTuple_false():
    Check(IsFlush, hand2d3d4d5d5s, None)

def test_flushTuple_true():
    Check(IsFlush, handldf, Card(16)) # 7-D

def test_straight_true1():
    Check(IsStraight, hands1, Card(38)) # Queen high straight

def test_straight_wrapped_1_true():
    Check(IsStraight, handws3, Card(51)) # 2S

def test_straight_wrapped_2_false():
    Check(IsStraight, handj1, None)

def test_straightflushTuple_true():
    Check(StraightFlushTuple, handldf, Card(16)) # 7-D

def test_straightflushTuple_true1():
    Check(IsStraightFlush, handldfmixedup, Card(19)) # 7-S
    
def test_straightflushTuple_false():
    Check(StraightFlushTuple, handws, None)

def test_fullHouse_true():
    Check(IsFullHouse, handfh, Card(6)) # 4H

def test_fullHouse_true2():
    Check(IsFullHouse, handws3, Card(2)) # 3H

def test_fullHouse_false():
    Check(IsFullHouse, handws, None)

def test_straight_performance():
    # testfunc = lambda *c: NumberDiffPred(c[0], c[1])
    #expected = [Card(38), Card(51), Card(16)]
    hands = [hands1, handws3, handldf]
    tests = [IsStraight, IsStraightFlush, IsFullHouse, IsXOfAKindTuple, IsFlush]
    testNumber = 0
    for test in tests:
        print("Testing: ", test.__name__)
        t0 = time.perf_counter()
        for hand in hands:
            st = createTupleHand(hand)
            print("Hand: {0}".format(st))

            # loop many times
            for i in range(10000):
                Execute(tests[testNumber], st)

            # test result against expected
            #if expected[test] is None:
            #    assert r is None
            #else:
            #    assert r == expected[test]
        t1 = time.perf_counter()
        d = t1-t0
        print("Time:{0}".format(d)) # 0.3
        testNumber += 1
    
    
test_straightflushTuple_true1()
test_straight_performance()