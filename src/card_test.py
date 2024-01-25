import random as r
import test
import time

import main
import hands
from Card import *

# tuple t = (1, 3, "c")
# set s = {"a", "b"}
# object = {}
# list = ["a", "b"]
# dict = {"a":1, "b": 2}

# comment
c = Card(39)
print("Testing Card Props for QS", c.name, c.value, c.number, c.suit)


def test_cardname():
    c = Card(38)
    if c.name != "Q-H":
        raise AssertionError


def create_hand(hand):
    hand.sort()
    return main.values_to_cards(hand)


def execute(f, hand):
    return f(hand)


def check(f, hand, expected):
    print("Testing: ", f.__name__)
    t0 = time.perf_counter()
    st = create_hand(hand)
    r = execute(f, st)
    t1 = time.perf_counter()
    d = t1 - t0
    print("Hand:{0}, Time:{1}\nResult:{2}".format(st, d, r))
    if r != expected:
        raise AssertionError


def test_triple_false2():
    check(main.is_x_of_a_kind, hands.hand2d3d4d5d5s, None)


def test_triple_true2():
    check(main.is_x_of_a_kind, hands.handt1, Card(34))  # JH


def test_flush_false():
    check(main.is_flush, hands.hand2d3d4d5d5s, None)


def test_flush_true():
    check(main.is_flush, hands.handldf, Card(16))  # 7-D


def test_straight_true1():
    check(main.is_straight, hands.hands1, Card(38))  # Queen high straight


def test_straight_wrapped_1_true():
    check(main.is_straight, hands.handws3, Card(51))  # 2S


def test_straight_wrapped_2_false():
    check(main.is_straight, hands.handj1, None)


def test_straight_flush_true():
    check(main.is_straight_flush, hands.handldf, Card(16))  # 7-D


def test_straight_flush_true1():
    check(main.is_straight_flush, hands.handldfmixedup, Card(19))  # 7-S


def test_straight_flush_false():
    check(main.is_straight_flush, hands.handws, None)


def test_full_house_true():
    check(main.is_full_house, hands.handfh, Card(6))  # 4H


def test_full_house_true2():
    check(main.is_full_house, hands.handws3, Card(2))  # 3H


def test_full_house_false():
    check(main.is_full_house, hands.handws, None)


def test_straight_performance():
    test_hands = [hands.hands1, hands.handws3, hands.handldf]
    tests = [
        main.is_straight,
        main.is_straight_flush,
        main.is_full_house,
        main.is_x_of_a_kind,
        main.is_flush,
    ]
    test_number = 0
    for test in tests:
        print("Testing: ", test.__name__)
        t0 = time.perf_counter()
        for hand in test_hands:
            st = create_hand(hand)
            print("Hand: {0}".format(st))

            # loop many times
            for i in range(10000):
                execute(tests[test_number], st)

            # test result against expected
            # if expected[test] is None:
            #    assert r is None
            # else:
            #    assert r == expected[test]
        t1 = time.perf_counter()
        d = t1 - t0
        print("Time:{0}".format(d))  # 0.3
        test_number += 1


test_straight_flush_true1()
test_straight_performance()
