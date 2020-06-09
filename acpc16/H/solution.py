
import math

'''
For given K, you may split the soldiers into K+1 shifts 
where 1 shift is off and the remaining K on duty. 
By looking at the pattern you can achive a closed form directly. 
'''

def solve(N, K):
    if N <= 1 or K == 0:
        return 0
    if N < K:
        return N - 1 
    if N % (K+1) == 0:
        return (N/(K+1)) * K
    return int( math.floor(N/(K+1))*K + (N-1)%(K+1) ) 



f = open("soldiers.in", "r")
output = open("soldiers.out", "r")


cases = int(next(f))
for i in range(1, cases+1): 
    
    line = (next(f)).split(" ")
    N, K = [int(i) for i in line]
    sol = solve(N,K)
    officialSol = int(next(output))
    if sol != officialSol:
        print(i,"Input", N, K)
        print("        -> ", sol- officialSol, sol)
    
