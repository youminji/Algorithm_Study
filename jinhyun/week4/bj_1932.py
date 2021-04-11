import sys

n = int(sys.stdin.readline())
dp = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = dp + temp

answer = 0

dp[1] = dp[0] + dp[1]
dp[2] = dp[0] + dp[2]



for j in range(2, n):
    up_first = j*(j-1)//2
    up_last = ((j+1)*j//2)-1
    now_first = (j+1)*j//2
    now_last = (j+1)*(j+2)//2-1
    for k in range(now_first, now_last+1):
        if k == now_first:
            dp[k] = dp[k] + dp[up_first]
            if answer < dp[k]:
                answer = dp[k]
        elif k == now_last:
            dp[k] = dp[k] + dp[up_last]
            if answer < dp[k]:
                answer = dp[k]
        else:
            dp[k] = dp[k] + max(dp[up_first+(k-now_first)], dp[up_first+(k-now_first)-1])
            if answer < dp[k]:
                answer = dp[k]

print(answer)

