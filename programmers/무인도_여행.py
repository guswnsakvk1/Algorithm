from collections import deque

def solution(maps):
    ## 세로 길이
    row = len(maps)
    ## 가로 길이
    col = len(maps[0])
    ## 해당 노드를 방문했는지 체크하는 리스트
    visited = [[False for j in range(col)] for i in range(row)]
    
    answer = bfs(maps, visited, row, col)
    
    return answer

def bfs(graph, visited, row, col):
    queue = deque()
    ## 숫자들의 합을 저장하는 함수
    lst = []
    
    ## 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
       
    for i in range(row):
        for j in range(col):
            ## 해당 위치가 길이 있고 방문하지 않았다면
            if graph[i][j] != 'X' and not visited[i][j]:
                ## 큐에 해당 위치 좌표 저장
                queue.append((i, j))
                ## 현재 위치 값으로 num 초기화
                num = int(graph[i][j])
                ## 현재 노드 방문처리
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    
                    ## 상하좌우로 이동
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        ## 범위가 넘어가거나 길이없으면 무시하고 계속 진행
                        if nx < 0 or ny < 0 or nx > (row - 1) or ny > (col - 1) or graph[nx][ny] == 'X':
                            continue
                        
                        ## 방문한 노드가 아니라면
                        if not visited[nx][ny]:
                            ## 큐에 좌표저장
                            queue.append((nx, ny))
                            ## num에 현재 위치 값 저장
                            num += int(graph[nx][ny])
                            ## 현재 노드 방문처리
                            visited[nx][ny] = True
                
                ## 답을
                lst.append(num)
    
    ## lst가 비었을 경우 답이 없기에 -1 리턴
    if not lst:
        return [-1]
    else:
        ## lst에 값이 있다면 정렬해서 리턴
        lst.sort()
        return lst