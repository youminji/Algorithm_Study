import sys

NaM = sys.stdin.readline().split()
number = list(map(int, sys.stdin.readline().split()))
N = int(NaM[0])
M = int(NaM[1])
number = sorted(number)
answer = []

def dfs(depth, last_number):
    if depth == M:
        for num in answer:
            print(num, end=' ')
        print()
        return
    else:
        for i in range (last_number, N):
            answer.append(number[i])
            dfs(depth + 1, i+1)
            answer.pop()

for j in range (N-M+1):
    answer.append(number[j])
    dfs(1, j+1)
    answer.pop()