
import Card as cd


def values_to_cards(hand):
    cards = []
    for v in hand:
        c = cd.Card(v)
        cards.append(c)
    return cards


def is_x_of_a_kind(cards, x=3, not_equal_to=-1):
    n1 = -1
    count = 0
    for c in cards:  # 0-3
        n2 = c.number
        if n2 > n1 or n2 == not_equal_to:
            count = 1
            n1 = n2
        else:
            count = count + 1
        if count == x:
            return c
    return None


def is_full_house(cards):
    t = is_x_of_a_kind(cards, 3)
    if t is not None:
        p = is_x_of_a_kind(cards, 2, t.number)
        if p is not None and t != p:
            return t
    return None


def is_flush(cards, x=5):
    for s in range(4):  # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in cards:
            if c.suit == s:
                count += 1
            if count == x:
                return c
    return None

# Pred: return 1 when true, -1 when false, 0 to ignore and continue


def number_diff_pred(c1, c2):
    diff = c2.number-c1.number
    if diff == 1 or diff == -12:
        return 1
    elif diff > 1:
        return -1
    return 0  # if diff = 0


def suit_equal_pred(c1, c2):
    if c2.suit == c1.suit:
        return 1
    return 0


def is_straight(cards, x=5, pred=lambda *c: number_diff_pred(c[0], c[1])):
    _count = 1
    _count_low = 0
    c1 = cards[0]
    first = c1
    for c in cards[1:]:  # 0-3, 0-11 [1:] start at 1
        p = pred(c1, c)
        if p == 1:
            _count += 1
        elif p == -1:
            if first.number == 0 and _count_low == 0:
                _count_low = _count
            _count = 1
        if _count == x:
            return c
        c1 = c
    if c1.number == 12 and _count + _count_low == x:  # n = 0-12 (12 = 2)
        return c1
    return None


def is_straight_flush(cards, x=5):
    for s in range(4):  # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        suitedCards = []
        for c in cards:
            if c.suit == s:
                suitedCards.append(c)
        if len(suitedCards) > 1:
            r = is_straight(suitedCards)
            if r is not None:
                return r
    return None
