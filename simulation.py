import random
import time
from main import *

p = 0
t = 0
s = 0
f = 0

startTime = time.perf_counter()

sims = 1000000
for h in range(sims):
    # random 13 card hand
    hand = random.sample(range(52), 13)


    if pair(hand):
        p = p +1
    if triple(hand):
        t = t + 1
    if straight(hand):
        s = s + 1
    if flush(hand):
        f = f +1

endTime = time.perf_counter()

duration = endTime - startTime
print(duration)

print ("Probabilities after {4} simulations: Pair ={0}, Triple={1}, Straight={2}, Flush={3}".format(p/sims,t/sims,s/sims,f/sims, sims))