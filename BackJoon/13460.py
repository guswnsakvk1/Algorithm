from collections import deque
import sys
input = sys.stdin.readline

def bfs(R_x, R_y, B_x, B_y, visited):
  visited[R_x][R_y][B_x][B_y] = True
  queue = deque([(R_x, R_y, B_x, B_y, 0)])

  while queue:
    x1, y1, x2, y2, num = queue.popleft()

    # num 10 이상이면 멈춤
    if num  > 9:
      print(-1)
      exit()

    for i in range(4):
      nx1 = x1
      ny1 = y1

      nx2 = x2
      ny2 = y2

      wall1, wall2 = False, False
      hole1, hole2 = False, False

      while True:
        # 앞에 벽이 없고
        # 구명에 빠지지 않은 경우
        # 빨간공 움직이기
        if not wall1 and not hole1:
          nx1 += dx[i]
          ny1 += dy[i]

        # 앞에 벽이 없는 경우
        # 파란공 움직이기
        if not wall2:
          nx2 += dx[i]
          ny2 += dy[i]

        # 현재 위치가 구멍인 경우
        # 빨간 공이 구멍에 빠지지 않는 경우
        if graph[nx1][ny1] == 'O' and not hole1:
          hole1 = True

        # 현재 위치가 구멍인 경우
        # 파란 공이 구멍에 빠지지 않은 경우
        if graph[nx2][ny2] == 'O' and not hole2:
          hole2 = True

        # 현재 위치가 벽인 경우
        # 빨간 공이 벽에 붇이치지 않은 경우
        if graph[nx1][ny1] == '#' and not wall1:
          wall1 = True
          nx1 -= dx[i]
          ny1 -= dy[i]

        # 현재 위치가 벽인 경우
        # 파란 공이 벽에 붇이치지 않은 경우
        if graph[nx2][ny2] == '#' and not wall2:
          wall2 = True
          nx2 -= dx[i]
          ny2 -= dy[i]

        # 빨간 공, 파란 공이 벽 앞에 있는 경우
        # 빨간 공, 파란 공 위치 좌표 쌍이 방문한 경우
        if wall1 and wall2 and visited[nx1][ny1][nx2][ny2]:
          break
        
        # 빨간 공, 파란 공이 벽 앞에 있는 경우
        # 빨간 공, 파란 공 위치 좌표 쌍이 방문하지 않은 경우
        if wall1 and wall2 and not visited[nx1][ny1][nx2][ny2]:
          queue.append((nx1, ny1, nx2, ny2, num+1))
          visited[nx1][ny1][nx2][ny2] = True
          break

        # 빨간 공이 벽 앞에 있고 파란 공이 바로 뒤에 있는 경우
        if wall1 and nx1 == nx2 and ny1 == ny2 and not visited[nx1][ny1][nx2-dx[i]][ny2-dy[i]]:
          queue.append((nx1, ny1, nx2-dx[i], ny2-dy[i], num+1))
          visited[nx1][ny1][nx2-dx[i]][ny2-dy[i]] = True
          break
        
        # 파란 공이 벽 앞에 있고 빨간 공이 바로 뒤에 있는 경우
        if wall2 and nx1== nx2 and ny1 == ny2 and not visited[nx1-dx[i]][ny1-dy[i]][nx2][ny2]:
          queue.append((nx1-dx[i], ny1-dy[i], nx2, ny2, num+1))
          visited[nx1-dx[i]][ny1-dy[i]][nx2][ny2] = True
          break
        
        # 파란 공이 구멍에 들어간 경우
        if hole2:
          break
        
        # 빨간 공이 구멍에 들어가고
        # 파란 공이 벽 앞에 있고
        # num이 9이상인 경우
        if hole1 and wall2 and num <= 9:
          print(num+1)
          exit()

  print(-1)

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(input().rstrip()))

visited = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]

R_x, R_y, B_x, B_y = 0, 0, 0, 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# R, B 위치 찾기
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'R':
      R_x = i
      R_y = j
      graph[i][j] = '.'

    if graph[i][j] == 'B':
      B_x = i
      B_y = j
      graph[i][j] = '.'

bfs(R_x, R_y, B_x, B_y, visited)