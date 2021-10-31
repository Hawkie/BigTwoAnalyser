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

c = Card(39)
print("Testing Card Props for QS",c.name,c.value, c.number, c.suit)

def test_cardname():
    c = Card(38)
    assert c.name == "Q-H"

#def a(f, c):
 #   f(c)

#c = Card(38)
#a(test_cardname, c)

def create_hand(hand):
    hand.sort()
    return values_to_cards(hand)

def execute(f, hand):
    return f(hand)

def check(f, hand, expected):
    print("Testing: ", f.__name__)
    t0 = time.perf_counter()
    st = create_hand(hand)
    r = execute(f, st)
    t1 = time.perf_counter()
    d = t1-t0
    print("Hand:{0}, Time:{1}\nResult:{2}".format(st, d, r))
    assert r == expected

def test_triple_false2():
    check(is_x_of_a_kind, hand2d3d4d5d5s, None)

def test_triple_true2():
    check(is_x_of_a_kind,handt1, Card(34)) # JH

def test_flush_false():
    check(is_flush, hand2d3d4d5d5s, None)

def test_flush_true():
    check(is_flush, handldf, Card(16)) # 7-D

def test_straight_true1():
    check(is_straight, hands1, Card(38)) # Queen high straight

def test_straight_wrapped_1_true():
    check(is_straight, handws3, Card(51)) # 2S

def test_straight_wrapped_2_false():
    check(is_straight, handj1, None)

def test_straight_flush_true():
    check(is_straight_flush, handldf, Card(16)) # 7-D

def test_straight_flush_true1():
    check(is_straight_flush, handldfmixedup, Card(19)) # 7-S
    
def test_straight_flush_false():
    check(is_straight_flush, handws, None)

def test_full_house_true():
    check(is_full_house, handfh, Card(6)) # 4H

def test_full_house_true2():
    check(is_full_house, handws3, Card(2)) # 3H

def test_full_house_false():
    check(is_full_house, handws, None)

def test_straight_performance():
    hands = [hands1, handws3, handldf]
    tests = [is_straight, is_straight_flush, is_full_house, is_x_of_a_kind, is_flush]
    testNumber = 0
    for test in tests:
        print("Testing: ", test.__name__)
        t0 = time.perf_counter()
        for hand in hands:
            st = create_hand(hand)
            print("Hand: {0}".format(st))

            # loop many times
            for i in range(10000):
                execute(tests[testNumber], st)

            # test result against expected
            #if expected[test] is None:
            #    assert r is None
            #else:
            #    assert r == expected[test]
        t1 = time.perf_counter()
        d = t1-t0
        print("Time:{0}".format(d)) # 0.3
        testNumber += 1
    
    
test_straight_flush_true1()
test_straight_performance()