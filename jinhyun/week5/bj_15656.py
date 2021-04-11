import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
answer = []

def dfs(depth):
    if depth == M:
        for num in answer:
            print(num, end=' ')
        print()
        return
    else:
        for i in range (N):
            answer.append(number[i])
            dfs(depth + 1)
            answer.pop()

for j in range (N):
    answer.append(number[j])
    dfs(1)
    answer.pop()