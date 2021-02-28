'''
    [BOJ] 2164 카드2
'''
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
deque = deque([x for x in range(1, N+1)])

while len(deque)>1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])