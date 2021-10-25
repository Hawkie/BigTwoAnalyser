import random
import time
from main import *
k2 = 0
k3 = 0
k4 = 0
s = 0
f = 0
sf = 0

t0 = time.perf_counter()
sims = 1000000
for h in range(sims):
    # random 13 card hand
    hand = random.sample(range(52), 13)
    hand.sort()
    st = HandToCardTuple(hand)

    if XOfAKindTuple(st,2):
        k2 = k2 + 1
    if XOfAKindTuple(st,3):
        k3 = k3 + 1
    if XOfAKindTuple(st,4):
        k4 = k4 + 1
    if StraightTuple(st):
        s = s + 1
    if flushTuple(st):
        f = f + 1
    if StraightFlushTuple(st):
        sf = sf + 1

t1 = time.perf_counter()
d = t1 - t0

print("Time to run={0} seconds".format(d))
print ("Probabilities after {0} simulations".format(sims))
print("Pair={0}\nTriple={1}\nFourOfAKind={2}\nStraight={3}\nFlush={4}".format(k2/sims,k3/sims,k4/sims,s/sims,f/sims))
print("StraightFlush={0}".format(sf/sims))