from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, visited, lst):
  # 현재 노드 방문한걸로 처리
  visited[i][j] = True
  
  ## 이동가능한 노드를 저장할 queue and tmp
  queue = deque()
  queue.append((i, j))
  tmp = [(i, j)]
  
  while queue:
    x, y = queue.popleft()

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      # 범위를 넘어가면 멈춤
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      # 현재 노드를 방문했다면 멈춤
      if visited[nx][ny]:
        continue

      # 두 노드의 차이가 L, R사이라면
      if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
        # queue에 nx, ny 넣기
        queue.append((nx, ny))
        # visited[nx][ny] 방문한걸로 처리
        visited[nx][ny] = True
        # tmp에 nx, ny 넣기
        tmp.append((nx, ny))
  
  # 만약 len(tmp)가 2보다 크면
  if len(tmp) >= 2:
    # lst에 tmp 넣기
    lst.append(tmp)

answer = 0
N, L, R = map(int, input().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:
  lst = []

  visited = [[False for _ in range(N)] for _ in range(N)]
  
  for i in range(N):
    for j in range(N):
      bfs(i, j, visited, lst)
  
  # lst가 없다면 
  # 국경을 열것이 없다는 것이므로
  # answer 출력
  if not lst:
    print(answer)
    break

  answer += 1
  
  # lst에 있는 list의
  for l in lst:
    num = 0
    # 모든 값을 num에 더한다
    for x, y in l:
      num += graph[x][y]

    # num을 l의 길이만큼 나누기
    num //= len(l)

    # l의 모든 graph값을
    # num으로 바꾸기
    for x, y in l:
      graph[x][y] = num