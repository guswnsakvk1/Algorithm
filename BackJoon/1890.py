import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

dp = [[0] *n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if dp[i][j] > 0 and board[i][j] > 0:
      x = i + board[i][j]
      y = j + board[i][j]

      if x <= n-1:
        dp[x][j] += dp[i][j]

      if y <= n-1:
        dp[i][y] += dp[i][j]

print(dp[n-1][n-1])