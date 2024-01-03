"""
1. 현재위치에서 먹을 수 있는 물고기 중 
   가장 가까운 물고기의 위치를 tmp에 저장
2. 만약 tmp가 있다면
   높고 왼쪽 기준으로 정렬 후 tmp[0] 번째 위치와 최소거리 return
3. 만약 tmp가 없다면
   빈 리스트 return
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

INF = 1e9
shark_size = 2
shark_eat = 0
answer = 0

def bfs(start_x, start_y):
  min_len = INF
  visited = [[False for j in range(n)] for i in range(n)]
  visited[start_x][start_y] = True
  queue = deque([])
  queue.append((start_x, start_y, 0))
  tmp = []

  while queue:
    x, y, num = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

      if graph[nx][ny] > shark_size:
        continue

      if visited[nx][ny]:
        continue

      if graph[nx][ny] == 0 or graph[nx][ny] == shark_size:
        visited[nx][ny] = True
        queue.append((nx, ny, num+1))
        continue

      if graph[nx][ny] < shark_size:
        visited[nx][ny] = True
        if min_len == INF:
          tmp.append((nx, ny))
          min_len = num + 1
        elif min_len == num + 1:
          tmp.append((nx, ny))
  
  if tmp:
    tmp.sort(key=lambda x : (x[0], x[1]))
    return [tmp[0][0], tmp[0][1], min_len]

  return tmp

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
      
find_start = False
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      start_x = i
      start_y = j
      graph[i][j] = 0
      find_start = True
      break

  if find_start:
    break

while True:
  lst = bfs(start_x, start_y)
  
  if lst:
    start_x = lst[0]
    start_y = lst[1]
    answer += lst[2]
    graph[lst[0]][lst[1]] = 0
  else:
    print(answer)
    break

  shark_eat += 1
  if shark_eat == shark_size:
    shark_size += 1
    shark_eat = 0