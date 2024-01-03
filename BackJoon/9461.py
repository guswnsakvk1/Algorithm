import sys
input = sys.stdin.readline

T = int(input())

lst = []

for i in range(T):
  lst.append(int(input()))

max_num = max(lst)

dp = [0,1,1,1,2,2]

for i in range(6, max_num+1):
  dp.append(dp[i-1] + dp[i-5])

for idx in lst:
  print(dp[idx])