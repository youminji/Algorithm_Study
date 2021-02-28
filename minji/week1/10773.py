'''
    [BOJ] 10773 제로
'''
import sys

N = int(sys.stdin.readline().rstrip())
s = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        s.pop()
    else:
        s.append(num)
ans = sum(x for x in s)
print(ans)
