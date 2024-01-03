from collections import deque

n, m, start = map(int, input().split())

## 2차 배열 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort()

## dfs 방법으로 방문한 노드인지 표시하는 배열
dfs_visited = [False] * (n + 1)
## dfs 정답
dfs_answer = []

## dfs 방법으로 노드 방문하는 함수
def dfs(graph, v, dfs_visited):
  ## 현재 노드는 방분했다고 True로 변경
  dfs_visited[v] = True
  dfs_answer.append(v)
  ## 현재 노드와 연결된 노드 중
  for i in graph[v]:
    ## 방문하지 않은 노드라면
    if not dfs_visited[i]:
      ## 방문
      dfs(graph, i, dfs_visited)

dfs(graph, start, dfs_visited)
print(" ".join(map(str, dfs_answer)))

## bfs 방법으로 방문한 노드인지 표시하는 배열
bfs_visited = [False] * (n + 1)
## bfs 정답
bfs_answer = []

## bfs 방법으로 노드 방문하는 함수
def bfs(graph, start, bfs_visited):
  ## 처음 시작하는 노드를 queue로 만들기
  queue = deque([start])
  ## 처음 시작하는 노드 방문처리
  bfs_visited[start] = True
  ## queue가 없어질때까지
  while queue:
    ## 방문한 노드 꺼내기
    v = queue.popleft()
    bfs_answer.append(v)
    ## 현재 노드와 연결된 노드들 중
    for i in graph[v]:
      ## 방문하지 않은 노드를
      if not bfs_visited[i]:
        ## queue에 저장
        queue.append(i)
        ## 방문처리
        bfs_visited[i] = True

bfs(graph, start, bfs_visited)
print(" ".join(map(str, bfs_answer)))