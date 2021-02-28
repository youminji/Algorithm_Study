'''
    [BOJ] 10866 덱
'''
import sys

N = int(sys.stdin.readline().rstrip())
deq = []

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push_front":
        deq.insert(0, cmd[1])
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] =="pop_front":
        if deq:
            print(deq.pop(0))
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)


