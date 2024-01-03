import copy
import sys
input = sys.stdin.readline

def dfs(room, cnt):
    if cnt == num:
        tmp = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    tmp += 1
        
        answer.append(tmp)
        return
    
    x, y = camera[cnt]
    camera_num = room[x][y]

    if camera_num == 1:
        result_room = up(copy.deepcopy(room), x, y)
        dfs(result_room, cnt+1)

        result_room = right(copy.deepcopy(room), x, y)
        dfs(result_room, cnt+1)

        result_room = down(copy.deepcopy(room), x, y)
        dfs(result_room, cnt+1)

        result_room = left(copy.deepcopy(room), x, y)
        dfs(result_room, cnt+1)
    elif camera_num == 2:
        result_room = up(copy.deepcopy(room), x, y)
        result_room = down(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = right(copy.deepcopy(room), x, y)
        result_room = left(result_room, x, y)
        dfs(result_room, cnt+1)
    elif camera_num == 3:
        result_room = up(copy.deepcopy(room), x, y)
        result_room = right(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = right(copy.deepcopy(room), x, y)
        result_room = down(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = down(copy.deepcopy(room), x, y)
        result_room = left(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = left(copy.deepcopy(room), x, y)
        result_room = up(result_room, x, y)
        dfs(result_room, cnt+1)
    elif camera_num == 4:
        result_room = up(copy.deepcopy(room), x, y)
        result_room = right(result_room, x, y)
        result_room = left(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = right(copy.deepcopy(room), x, y)
        result_room = down(result_room, x, y)
        result_room = up(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = down(copy.deepcopy(room), x, y)
        result_room = left(result_room, x, y)
        result_room = right(result_room, x, y)
        dfs(result_room, cnt+1)

        result_room = left(copy.deepcopy(room), x, y)
        result_room = down(result_room, x, y)
        result_room = up(result_room, x, y)
        dfs(result_room, cnt+1)
    elif camera_num == 5:
        result_room = up(copy.deepcopy(room), x, y)
        result_room = right(result_room, x, y)
        result_room = down(result_room, x, y)
        result_room = left(result_room, x, y)
        dfs(result_room, cnt+1)


# 위 감시
def up(room, x, y):
    while x-1 > -1:
        x -= 1
        
        if room[x][y] == 0:
            room[x][y] = '#'
        elif room[x][y] == 6:
            break
        
    return room

# 오른쪽 감시
def right(room, x, y):
    while y+1 < M:
        y += 1

        if room[x][y] == 0:
            room[x][y] = '#'
        elif room[x][y] == 6:
            break
        
    return room
        
# 아래 감시
def down(room, x, y):
    while x+1 < N:
        x += 1
        
        if room[x][y] == 0:
            room[x][y] = '#'
        elif room[x][y] == 6:
            break
        
    return room
        
# 왼쪽 감시
def left(room, x, y):
    while y-1 > -1:
        y -= 1
        
        if room[x][y] == 0:
            room[x][y] = '#'
        elif room[x][y] == 6:
            break
        
    return room

N, M = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

# 카메라가 있는 위치 찾기
camera = []
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5:
            camera.append((i, j))

num = len(camera)
answer = []

dfs(room, 0)
print(min(answer))