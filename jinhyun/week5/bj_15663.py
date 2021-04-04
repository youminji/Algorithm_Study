import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
visit = [0 for t in range (N)]
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
            if visit[i] == 0:
                answer = answer + ' ' + str(number[i])
                visit[i] = 1
                dfs(depth + 1)
                visit[i] = 0
                answer= answer[:-len(str(number[i]))-1]

for j in range (N):
    visit[j] = 1
    answer = str(number[j])
    dfs(1)
    visit[j] = 0
    answer= answer[:-len(str(number[j]))]

for ans in check:
    print(ans)