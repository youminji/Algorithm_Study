import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
global answer
check = {}

def dfs(depth, last_number):
    if depth == M:
        global answer
        if answer not in check:
            check[answer] = True
        return
    else:
        for i in range (last_number, N):
            answer = answer + ' ' + str(number[i])
            dfs(depth + 1, i+1)
            answer= answer[:-len(str(number[i]))-1]

for j in range (N-M+1):
    answer = str(number[j])
    dfs(1, j+1)
    answer= answer[:-len(str(number[j]))]

for ans in check:
    print(ans)