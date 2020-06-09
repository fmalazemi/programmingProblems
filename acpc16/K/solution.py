

import math

def solve(G, C, E):
    if C > E: 
        return 0
    if G == 2:
        G = 3
    elif G == 3:
        G = 5
    return math.ceil((E-C)*G)


f = open("pokemon.in")
out = open("pokemon.out")

N = int(next(f))
while N > 0:

    line = next(f)
    G, C, E = [int(i) for i in line.split(" ")]
    sol = solve(G, C, E)
    officailSol = int(next(out))
    if sol != officailSol:
        print("Input ", G, C, E)
        print("----->", sol, officailSol)

    N -= 1