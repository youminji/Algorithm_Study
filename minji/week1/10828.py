'''
    [BOJ] 10828 스택
'''
import sys
N = int(sys.stdin.readline().rstrip())
s = []
for _ in range(0,N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push":
        s.append(cmd[1])
    elif cmd[0] == "pop":
        #if len(s) == 0:
        if (not s):
            print(-1)
        else:
            print(s.pop())
    elif cmd[0] == "size":
        print(len(s))
    elif cmd[0] == "empty":
        #if len(s) == 0:
        if (not s):
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if s:
            print(s[-1])
        else:
            print(-1)



