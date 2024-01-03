from collections import deque
import sys
input = sys.stdin.readline

def bfs(cheese, cnt):
  queue = deque([(0,0)])
  remove_cheese = set([])
  visited = [[False] * M for _ in range(N)]
  visited[0][0] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

      if visited[nx][ny]:
        continue

      if cheese[nx][ny]:
        remove_cheese.add((nx, ny))
      else:
        queue.append((nx, ny))

      visited[nx][ny] = True

  for x, y in remove_cheese:
    cheese[x][y] = 0

  return cnt - len(remove_cheese)

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

time = 0
cnt = 0
for i in range(N):
  for j in range(M):
    if cheese[i][j]:
      cnt += 1

while True:
  tmp = bfs(cheese, cnt)
  time += 1
  if tmp:
    cnt = tmp
  else:
    break

print(time)
print(cnt)