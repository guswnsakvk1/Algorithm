from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    tmp = []
    
    while queue:
        x, y = queue.popleft()
        cnt = 0

        if x == 0 or x == N-1 or y == 0 or y == M-1:
                continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if visited[nx][ny]:
                continue
            
            if ice[nx][ny] == 0:
                cnt += 1
            else:
                visited[nx][ny] = True
                queue.append((nx, ny))

        tmp.append((x,y,cnt))

    for x, y, cnt in tmp:
        ice[x][y] = max(0, ice[x][y] - cnt)
            
N, M = map(int, input().split())

ice = []
for _ in range(N):
    ice.append(list(map(int, input().split())))

year = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:
    cnt = 0
    visited = [[False for j in range(M)] for i in range(N)]

    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] != 0 and not visited[i][j]:
              bfs(i,j,visited)
              cnt += 1

    if cnt >= 2:
        break
    elif cnt == 0:
        print(0)
        exit()
    else:
        year += 1

print(year)