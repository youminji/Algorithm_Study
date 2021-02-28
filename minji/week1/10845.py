'''
    [BOJ] 10845 큐 
'''
import sys
N = int(sys.stdin.readline().rstrip())
q = []

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if (not q):
            print(-1)
        else:
            print(q.pop(0))
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)


