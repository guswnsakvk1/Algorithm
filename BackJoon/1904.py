import sys
input = sys.stdin.readline

N = int(input())

dp = [1,2]

for i in range(2, N):
    dp.append((dp[i-1] + dp[i-2]) % 15746)

print(dp[N-1])