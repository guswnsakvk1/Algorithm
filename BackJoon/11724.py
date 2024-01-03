from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

## 2차 배열 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

## 방문한 노드인지 확인
visited = [False] * (n + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

answer = 0
## 1~n 까지의 노드를 방문했는지 확인
for i in range(1, n+1):
    ## 방문하지 않았다면 bfs로 연결된 노드 확인
    if not visited[i]:
        bfs(graph, i, visited)
        answer += 1

print(answer)