def dfs(x,y,visited):
    if y == k-1:
        return True
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1

        if nx < 0 or nx >= n or ny < 0 or ny >= k:
            continue
        
        if visited[nx][ny]:
            continue
        
        if gas[nx][ny] == '.':
            visited[nx][ny] = True
            if dfs(nx, ny, visited):
                return True

    return False

n, k = map(int, input().split())
answer = 0

gas = []
for _ in range(n):
    gas.append(list(input()))

dx = [-1, 0, 1]

visited = [[False for j in range(k)] for i in range(n)]

for i in range(n):
    if dfs(i, 0, visited):
        answer += 1

print(answer)