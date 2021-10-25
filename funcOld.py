def suit(x):
    return x%4

def number(x):
    return int(x/4)


def pair(hand):
    for i in range(len(hand)-1): #0-3
        first = hand[i]
        for j in range(len(hand)-i-1): #0-3, 0-2, 0-1, 0
            second = hand[j+i+1]
            if number(first) == number(second):
                return True
    return False

def triple(hand):
    for i in range(len(hand)-1): #0-3
        first = hand[i]
        for j in range(len(hand)-i-1): #0-3, 0-2, 0-1, 0
            second = hand[j+i+1]
            for k in range(len(hand)-i-j-2): #0-2, 0-1, 0
                third = hand[k+j+i+2]
                if number(first) == number(second) == number(third):
                    return True
    return False

def flush(hand, x=5):
    for s in range(4): # suits 0-3 0 = diamonds, 1 = clubs, 2 = hearts, 3 = spades
        count = 0
        for c in hand:
            if suit(c) == s:
                count = count +1
            if count == x:
                return True
    return False

def straight(hand, x=5):
    h2 = hand.copy()
    h2.sort()
    count = 0
    countLow = -1
    fc = h2[0]
    indexArray = [*range(1,len(h2))]
    c1=number(fc)
    first = c1
    for c in indexArray: # 0-3, 0-11
        c2=number(h2[c]) # 1-4, 1-12
        diff = c2-c1
        #print("{0}, {1}, {2}".format(c1,c2, diff))
        if diff == 1:
            count = count+1
        elif diff == -12: # allow for wrap around straights (e.g. KA234) 
            count = count +1
        elif diff > 1:
            if first == 0:
                if countLow == -1:
                    countLow = count
            count = 0
        if count == x-1:
            return True
        c1 = c2
    #print("no straight in ", h2)
    if c2 == 12:
        if count + countLow == x-2:
            return True
    return False