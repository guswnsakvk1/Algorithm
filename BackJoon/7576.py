from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
## 현재 노드의 좌표와 몇 번 반복된 것인지 저아
global queue
global answer
queue = deque()
answer = 0
## 답을 출력할 때
## graph에 0이 있으면 -1을 출력
flag = False

## 2차 배열 만들기
graph = []
for i in range(m):
    lst = list(map(int,input().split()))
    graph.append(lst)
    ## bfs처음에 시작할 때
    ## 1인 곳에서 동시에 시작해야 하기에
    ## 1인 곳을 찾기
    for j in range(n):
        if lst[j] == 1:
            queue.append((i, j, 0))

## 좌표의 변화를 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, dx, dy):
    global queue
    global answer

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            ## 범위가 넘었을 경우 무시하고 계속 진행
            if nx < 0 or ny < 0 or nx > (m-1) or ny > (n-1):
                continue
            
            ## 현재 노드가 0이면 1로 바꾸기
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                answer = max(answer, cnt + 1)
                queue.append((nx, ny, cnt + 1))

bfs(graph, dx, dy)

## 현재 그래프에서 0이 있는지 확인
for i in graph:
    if 0 in i:
        flag = True
    
    if flag:
        break

## flag가 True이면 -1출력
## False이면 answer 출력
if flag:
    print(-1)
else:
    print(answer)