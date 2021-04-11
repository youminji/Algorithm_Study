import sys
dp = []
T = int(sys.stdin.readline())
dp.append(1)
dp.append(2)
dp.append(4)

for i in range(3, 11):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])


for i in range(T):
    n = int(sys.stdin.readline())
    print(dp[n-1])
            
