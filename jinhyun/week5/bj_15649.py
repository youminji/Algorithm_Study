import sys

number = sys.stdin.readline().split()
N = int(number[0])
M = int(number[1])
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
                answer.append(i+1)
                visit[i] = 1
                dfs(depth + 1)
                visit[i] = 0
                answer.pop()

for j in range (N):
    visit[j] = 1
    answer.append(j+1)
    dfs(1)
    visit[j] = 0
    answer.pop()