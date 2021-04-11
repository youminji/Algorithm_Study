import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
global answer
check = {}

def dfs(depth):
    if depth == M:
        global answer
        if answer not in check:
            check[answer] = True
        return
    else:
        for i in range (N):
            answer = answer + ' ' + str(number[i])
            dfs(depth + 1)
            answer= answer[:-len(str(number[i]))-1]

for j in range (N):
    answer = str(number[j])
    dfs(1)
    answer= answer[:-len(str(number[j]))]

for ans in check:
    print(ans)