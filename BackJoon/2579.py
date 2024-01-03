import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  lst.append(int(input()))

if n < 3:
  print(sum(lst))
else:
  dp = []
  dp.append(lst[0])
  dp.append(max(lst[0] + lst[1], lst[1]))
  dp.append(max(lst[0] + lst[2], lst[1] + lst[2]))

  for i in range(3, n):
    dp.append(max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i]))

  print(dp[-1])