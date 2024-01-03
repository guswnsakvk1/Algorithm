import sys

input = sys.stdin.readline

N = int(input())

lst = []
dp = [0] * (N + 1)

for _ in range(N):
  T, P = map(int, input().split())
  lst.append((T, P))

for i in range(1, N + 1):
  T, P = lst[i - 1]

  if i + T  <= N+1:
    dp[i] += P
    for j in range(i+T, N+1):
      dp[j] = max(dp[j], dp[i])

print(max(dp))