import random
import time
from main import *
k2 = 0
k3 = 0
k4 = 0
full hfh = 0
s = 0
f = 0
sf = 0

t0 = time.perf_counter()
sims = 10000
for h in range(sims):
    # random 13 card hand
    hand = random.sample(range(52), 13)
    hand.sort()
    st = ValuesToCards(hand)

    if XOfAKindTuple(st,2) != -1:
        k2 += 1
    if XOfAKindTuple(st,3) != -1:
        k3 += 1
    if XOfAKindTuple(st,4) != -1:
        k4 += 1
    if FullHouse(st) != -1:
        fh += 1
    if StraightTuple(st):
        s += 1
    if FlushTuple(st):
        f += 1
    if StraightFlushTuple(st):
        sf += 1

t1 = time.perf_counter()
d = t1 - t0

print("Time to run {0} simulations was seconds {1}".format(sims, d))
print("Pair={0}\nTriple={1}\nFourOfAKind={2}".format(k2/sims,k3/sims,k4/sims))
print("FullHouse={0}\nStraight={1}\nFlush={2}".format(fh/sims,s/sims,f/sims))
print("StraightFlush={0}".format(sf/sims))