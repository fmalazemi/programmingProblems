
'''
A simple BFS with few tricks. 

1. DFS won't work cuz you want to find 
   shortest path and the tree depth is 
   very long
2. A special solution when M = 1
3. The state is (curValue, curString)
4. Next state for A*M^2 + B*M^1 + C 
	-> M*(A*M^2 + B*M^1 + C )+ D

'''





from collections import deque

def getFullSol(sol, L):
	
	if sol == "None" or len(sol) > L:
		return sol
	while len(sol) != L:
		sol = "A" + sol
	return sol

d = 1
def bfs(L, H, M): 
	mod = 10007
	LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if H < len(LETTERS):
		return getFullSol(LETTERS[H], L)
	if M == 0 or L == 1:
		return "None"

	isSeen = {}
	q = deque()
	for i in range(26):
		q.append((i,  LETTERS[i]))
		isSeen[i] = True 
	
	while q:
		curValue, curSol = q.popleft()
		for i in range(26):
			nextValue = (curValue*M + i) % mod
			if curValue == H:
				return getFullSol(curSol, L) 
			if nextValue not in  isSeen and len(curSol) < L:
				# little optimization to reduce the size of the queue
				q.append((nextValue,  curSol + LETTERS[i] ))
				isSeen[nextValue] = True 
	return "None"
					

f = open("code.in", "r")
output = open("code.out", "r")
cases = int(next(f))
for i in range(cases):
	line = next(f)
	L, H, M = line.split(" ")
	L, H, M = int(L), int(H), int(M)

	sol = bfs(L, H, M)
	officialSol = next(output)

	while ord(officialSol[0]) == 0:
		officialSol = officialSol[1:]
	officialSol = officialSol[:-1]
	if sol != officialSol:
		print(i+1, "input ->", L, H, M)
		print(i+1, "False", sol[len(sol)-30:], officialSol[len(officialSol)-30:])
		print(len(sol), len(officialSol))
