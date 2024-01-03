from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

answer = 1e9
house = []
chicken = []

for i in range(n):
  lst = list(map(int, input().split()))
  for j in range(n):
    if lst[j] == 1:
      house.append((i, j))

    if lst[j] == 2:
      chicken.append((i, j))

for live_chicken in combinations(chicken, m):
  memo = [100] * len(house)

  for i, h in enumerate(house):
    for live in live_chicken:
      if memo[i] > abs(h[0] - live[0]) + abs(h[1] - live[1]):
        memo[i] = abs(h[0] - live[0]) + abs(h[1] - live[1])

  if answer > sum(memo):
    answer = sum(memo)
  
print(answer)