
from collections import defaultdict


def getRange(L):
    maxList = [ max(i) for i in L ]
    minList = [ min(i) for i in L ]
    maxList = [min(maxList), max(maxList)] 
    minList = [min(minList), max(minList)] 
    if maxList[0] <= minList[1]:
        return [maxList[0], minList[1]]
    return False 


def solve(q, overlapRange):
    if overlapRange == False:
        return "NOT SURE"
    if  overlapRange[0] <= q <= overlapRange[1]:
        return "YES"
    return "NOT SURE"

f = open("shikabika.in")
out = open("shikabika.out")

T = int(next(f))
i = 0   
count = 0
for i in range(T):
    N, Q = [int(i) for i in (next(f)).split(" ")]
    L = []
    while N > 0:
        shika, bika = (next(f)).split(" ")
        L.append([int(shika), int(bika)])
        N -= 1
    overlapRange = getRange(L)

    while Q > 0:
        q = int(next(f))
        offcialSol = next(out)
        sol = solve(q, overlapRange)
        if sol not in offcialSol:
            print( q, overlapRange, offcialSol)
        Q -= 1

