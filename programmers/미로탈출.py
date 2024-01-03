from collections import deque

def solution(maps):
    ## 시작 위치
    start_point = find_start(maps)
    ## 레버 위치
    lever_point = find_lever(maps)
    ## 시작 -> 레버 최소거리
    start_to_lever = bfs(start_point, maps, 'L')
    ## 레버 -> 출구 최소거리
    lever_to_exit = bfs(lever_point, maps, 'E')
    
    ## 시작 또는 레버 중에 -1이 있으면 -1리턴
    if start_to_lever == -1 or lever_to_exit == -1:
        return -1
    return start_to_lever + lever_to_exit

## 시작위치 찾기
def find_start(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                return [i, j]

## 레버위치 찾기   
def find_lever(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                return [i, j]
            
def bfs(start, maps, target):
    start_row, start_col = start
    # print('start_row : ' + str(start_row))
    # print('start_col : ' + str(start_col))
    
    queue = deque()
    queue.append((start_row, start_col, 0))
    
    row = len(maps)
    col = len(maps[0])
    
    # print('row : ' + str(row))
    # print('col : ' + str(col))
    
    ## 갔던 길인지 저장하는 2차 배열
    visited = [[False for j in range(col)] for i in range(row)] 
    visited[start_row][start_col] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0,- 1, 1]
    
    distance = 1e9
    
    # print('visited : ' + str(visited))
    
    while queue:
        now_row, now_col, cnt = queue.popleft()
        # print(now_row, now_col, cnt)
        
        for i in range(4):
            new_row = now_row + dx[i]
            new_col = now_col + dy[i]
            
            ## 범위를 넘어가거나 길이 없으면 무시하고 계속 진행
            if new_row < 0 or new_col < 0 or new_row > (row - 1) or new_col > (col - 1) or maps[new_row][new_col] == 'X':
                continue
            
            ## 현재 위치가 간 곳이 아니라면
            if not visited[new_row][new_col]:
                ## 현재 위치를 간곳으로 저장
                visited[new_row][new_col] = True
                ## 우리가 찾는 타켓을 찾으면 비교
                if maps[new_row][new_col] == target:
                    distance = min(distance, cnt)
                else:
                    ## 아니면 queue에 넣기
                    queue.append((new_row, new_col, cnt + 1))

                ## 밑에 코드로 돌리면 모든 케이스가 탐색이 안됨
                # if maps[new_row][new_col] == 'O':
                #     queue.append((new_row, new_col, cnt + 1))
                # elif maps[new_row][new_col] == target:
                #     distance = min(distance, cnt)
                    
    if distance == 1e9:
        return -1
    else:
        return distance + 1