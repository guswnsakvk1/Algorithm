from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
  queue = deque([(i, j)])
  graph[i][j] = 0

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(T):
  n, m, k = map(int, input().split())

  graph = [[0 for j in range(m)] for i in range(n)]

  for i in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

  answer = 0
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        bfs(i, j)
        answer += 1

  print(answer)