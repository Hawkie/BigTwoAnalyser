import random as r
import test
import time

from funcOld import *
from hands import *

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
    r = straight(hand)
    t1 = time.perf_counter()
    d = t1-t0
    print("Time:", d)
    assert r == expected


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

def test_triple_true1():
    checktriple(handt1, True)

    
def test_flush_falsej():
    checkflush(handj1, False)

def test_flush_false():
    checkflush(hand2d3d4d5d5s, False)

def test_flush_true():
    checkflush(handldf, True)


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
    checkstraight(handnws2, False)

def test_straight_wrapped_true3():
    checkstraight(handws3, True)

