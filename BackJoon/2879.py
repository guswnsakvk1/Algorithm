import sys

input = sys.stdin.readline

N = int(input())
before = list(map(int, input().split()))
after = list(map(int, input().split()))

answer = 0
gap = []
dp = [0] * N

for i in range(N):
  gap.append(after[i] - before[i])

dp[0] = abs(gap[0])

for i in range(1, N):
  if gap[i] * gap[i-1] > 0:
    dp[i] = dp[i-1] + max(0, abs(gap[i]) - abs(gap[i-1]))
  else:
    dp[i] = dp[i-1] + abs(gap[i])

print(dp[N-1])