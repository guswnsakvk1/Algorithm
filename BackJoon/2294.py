import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0] * (k+1)

for i in range(1, k+1):
    for coin in coins:
        if i - coin >= 0:
            if i == coin:
                dp[i] = 1
            elif dp[i-coin]:
                if dp[i]:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                else:
                    dp[i] = dp[i-coin] + 1
        else:
            break

if dp[-1]:
    print(dp[-1])
else:
    print(-1)