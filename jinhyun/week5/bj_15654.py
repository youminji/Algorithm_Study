import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
visit = [0 for t in range (N)]
answer = []

def dfs(depth):
    if depth == M:
        for num in answer:
            print(num, end=' ')
        print()
        return
    else:
        for i in range (N):
            if visit[i] == 0:
                answer.append(number[i])
                visit[i] = 1
                dfs(depth + 1)
                visit[i] = 0
                answer.pop()

for j in range (N):
    visit[j] = 1
    answer.append(number[j])
    dfs(1)
    visit[j] = 0
    answer.pop()