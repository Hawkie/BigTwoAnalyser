import random
import time
from main import *

k2 = 0
k3 = 0
k4 = 0
fh = 0
s = 0
f = 0
sf = 0

t0 = time.perf_counter()
sims = 1000000
print("Running {0} simulations for probabilities".format(sims))
for h in range(sims):
    # random 13 card hand
    hand = random.sample(range(52), 13)
    hand.sort()
    st = values_to_cards(hand)

    if is_x_of_a_kind(st, 2) is not None:
        k2 += 1
    if is_x_of_a_kind(st, 3) is not None:
        k3 += 1
    if is_x_of_a_kind(st, 4) is not None:
        k4 += 1
    if is_full_house(st) is not None:
        fh += 1
    if is_straight(st) is not None:
        s += 1
    if is_flush(st) is not None:
        f += 1
    if is_straight_flush(st) is not None:
        sf += 1

t1 = time.perf_counter()
d = t1 - t0

print("Time to run {0} simulations was seconds {1}".format(sims, d))
print("Pair={0}\nTriple={1}\nFourOfAKind={2}".format(k2 / sims, k3 / sims, k4 / sims))
print("FullHouse={0}\nStraight={1}\nFlush={2}".format(fh / sims, s / sims, f / sims))
print("StraightFlush={0}".format(sf / sims))
