from collections import deque
import copy
import sys
input = sys.stdin.readline

def solve(graph, air_place):
  dust = find_dust(graph)
  tmp = copy.deepcopy(graph)

  while dust:
    x, y, num = dust.popleft()
    cnt = 0
    num //= 5

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= R or ny < 0 or ny >= T:
        continue

      if graph[nx][ny] != -1:
        cnt += 1
        tmp[nx][ny] += num

    tmp[x][y] -= num * cnt
  
  wind_up(tmp, air_place[0])
  wind_down(tmp, air_place[1])

  return tmp


def find_air(graph):
  for i in range(R):
    for j in range(T):
      if graph[i][j] == -1:
        return [i, i + 1]


def find_dust(graph):
  queue = deque([])

  for i in range(R):
    for j in range(T):
      if graph[i][j] >= 5:
        queue.append((i, j, graph[i][j]))

  return queue


def wind_up(tmp, air_place):
  num = tmp[air_place][1]

  for i in range(2, T):
    tmp[air_place][i], num = num, tmp[air_place][i]

  for i in range(air_place-1, -1, -1):
    tmp[i][T-1], num = num, tmp[i][T-1]
  
  for i in range(T-2, -1, -1):
    tmp[0][i], num = num, tmp[0][i]

  for i in range(1, air_place):
    tmp[i][0], num = num, tmp[i][0]

  tmp[air_place][1] = 0

def wind_down(tmp, air_place):
  num = tmp[air_place][1]

  for i in range(2, T):
    tmp[air_place][i], num = num, tmp[air_place][i]

  for i in range(air_place+1, R):
    tmp[i][T-1], num = num, tmp[i][T-1]

  for i in range(T-2, -1, -1):
    tmp[R-1][i], num = num, tmp[R-1][i]

  for i in range(R-2, air_place, -1):
    tmp[i][0], num = num, tmp[i][0]

  tmp[air_place][1] = 0

R, T, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

air_place = find_air(graph)

for i in range(C):
  graph = copy.deepcopy(solve(graph, air_place))

answer = 2
for g in graph:
  answer += sum(g)

print(answer)