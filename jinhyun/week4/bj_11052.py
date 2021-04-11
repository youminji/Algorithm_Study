import sys

N = int(sys.stdin.readline())

dp = list(map(int, sys.stdin.readline().rstrip().split()))

for j in range(1, N):
    for k in range(0,j):
        dp[j] = max(dp[j], dp[j-k-1]+dp[k])
    
print(dp[N-1])