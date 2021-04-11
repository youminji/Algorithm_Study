import sys

global answer
global visit

def dfs(c_depth, k, s, last_index):
    global answer
    if c_depth == 5:
        for num in answer:
            print(num, end=' ')
        print()
        return
    else:
        for i in range (last_index+1, k):
            if visit[i] == 0:
                visit[i] = 1
                answer.append(s[i])
                dfs(c_depth+1, k, s, i)
                visit[i] = 0
                answer.pop()
            


while True:
    t = sys.stdin.readline().split()
    if t[0] == '0':
        break
    else:
        k = int(t[0])
        s = list(map(int, t[1:]))
        visit = [0 for p in range(k)]
        global answer
        answer = []
        for j in range (k-6+1):
            visit[j] = 1
            answer.append(s[j])
            dfs(0, k, s, j)
            visit[j] = 0
            answer.pop()
    print()