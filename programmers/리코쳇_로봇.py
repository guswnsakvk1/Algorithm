""" 
1. 벽(D)에 부딪치거나 board의 범위를 넘어갈 때 전 위치를 저장
-> 포켓몬스터에 나오는 얼음관장 이동을 생각
-> 벽에 부딪치면 벽을 통과하지 못함

2. 벽에 부딧치면 현재 위치를 간 적이 없다면 출발한 곳의 visited의 값에 +1한 값을 저장

3. 현재 위치를 간 적이 있다면 저장할 필요없이 계속 진행
-> 저 적은 횟수로 현재 위치에 도달할 수 있기에 저장할 필요없음
"""

from collections import deque

def solution(board):
    x_len = len(board)
    y_len = len(board[0])
    start = find_start(board, x_len, y_len)
    answer = bfs(board, x_len, y_len, start[0], start[1])
    
    return answer - 1 if answer > 0 else -1

def find_start(board, x_len, y_len):
    for i in range(x_len):
        for j in range(y_len):
            if board[i][j] == "R":
                return [i, j]
            
def bfs(board, x_len, y_len, x_start, y_start):
    queue = deque()
    queue.append((x_start, y_start))
    
    visited = [[0 for j in range(y_len)] for i in range(x_len)]
    visited[x_start][y_start] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y = queue.popleft()
        
        if board[x][y] == 'G':
            return visited[x][y]
        
        for i in range(4):
            nx = x
            ny = y
            
            while True:
                nx += dx[i]
                ny += dy[i]
            
                if 0 <= nx < x_len and 0 <= ny < y_len and board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                
                if nx < 0 or nx >= x_len or ny < 0 or ny >= y_len:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
        
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        
    return -1