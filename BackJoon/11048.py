import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maze = []
for _ in range(n):
  maze.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]
dp[0] = maze[0]

for i in range(n):
  for j in range(m):
    if i != n-1:
      if j == m-1:
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + maze[i+1][j])
      else:
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + maze[i+1][j])
        dp[i][j+1] = max(dp[i][j+1], dp[i][j] + maze[i][j+1])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + maze[i+1][j+1])
    else:
      if j == m-1:
        print(dp[n-1][m-1])
      else:
        dp[i][j+1] = max(dp[i][j+1], dp[i][j] + maze[i][j+1])