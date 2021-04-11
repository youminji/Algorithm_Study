import sys

number = sys.stdin.readline().split()
N = int(number[0])
M = int(number[1])
answer = []

def dfs(depth, last_number):
    if depth == M:
        for num in answer:
            print(num, end=' ')
        print()
        return
    else:
        for i in range (last_number, N):
            answer.append(i+1)
            dfs(depth + 1, i)
            answer.pop()

for j in range (N):
    answer.append(j+1)
    dfs(1, j)
    answer.pop()