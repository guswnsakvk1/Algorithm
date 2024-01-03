from collections import deque

def solution(maps):
    answer = bfs(maps, len(maps), len(maps[0]))
    
    return -1 if answer==1 else answer

def bfs(graph, x_end, y_end):    
    ## 상하좌우 이동
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            ## 범위를 넘어가면 무시하고 진행
            if nx < 0 or ny < 0 or nx >= x_end or ny >= y_end:
                continue
            
            ## 벽이면 무시하고 진행
            if graph[nx][ny] == 0:
                continue
            
            ## 길이 있으면
            if graph[nx][ny] == 1:
                ## 현재 노드에 전노드값에 +1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            
    return graph[x_end-1][y_end-1]