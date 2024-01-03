from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
  queue = deque([(i, j)])
  graph[i][j] = 0
  num = 1

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = 0
        num += 1

  answer.append(num)

n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

answer = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i, j)

print(len(answer))
answer.sort()
for a in answer:
  print(a)