import sys
input = sys.stdin.readline

def dfs(x, y):
  if dp[x][y] == -1:
    dp[x][y] = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if graph[nx][ny] > graph[x][y]:
        dp[x][y] += dfs(nx, ny)

  return dp[x][y]

n, m = map(int, input().split())

graph = [[0]*(m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0]*(m+2)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dp = [[-1]*(m+2) for _ in range(n+2)]
dp[1][1] = 1

print(dfs(n, m))