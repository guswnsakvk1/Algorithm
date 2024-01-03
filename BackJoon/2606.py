## 1번 노드와 연결된 노드는 바이러스에 감염되는 것이므로
## dfs를 활용해서 1번 노드부터 시작해서 연결된 노드 개수 확인
## 답을 출력할 때는 1번 노드도 포함한 값이기에 -1을 해줘야함

n = int(input())
m = int(input())
global answer
answer = 0

## 2차 배열 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

## 노드 방문 여부 확인 배열
visited = [False] * (n + 1)

def dfs(graph, v, visited):
    global answer
    if not visited[v]:
        visited[v] = True
        answer += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(answer - 1)