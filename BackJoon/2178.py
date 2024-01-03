from collections import deque

n, m = map(int, input().split())

## 2차 배열 만들기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

## 상, 하, 좌, 우 좌표 변화
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    ## queue에 x, y 좌표 저장
    queue = deque()
    queue.append((x, y))
    
    ## queue가 빌떄까지
    while queue:
        ## x, y 좌표를 뽑고
        x, y = queue.popleft()
        ## 상, 하, 좌, 우로 좌표 이동시켜보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ## 이동시킨 좌표가 범위를 넘어가면 무시하고 계속 진행
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            
            ## 이동시킨 좌표가 벽이면 무시하고 계속 진행
            if graph[nx][ny] == 0:
                continue
            
            ## 이동시킨 좌표에 이동시키전 좌표 + 1
            ## 이동시킨 좌표 queue에 좌표 저장
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))