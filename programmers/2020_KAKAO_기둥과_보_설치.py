"""
- can_pillar
1. 기둥이 바닥에 설치되는 경우 : y == 0
2. 기둥 위에 기둥이 설치되는 경우 : pillar[x][y-1]
3. 보의 한쪽 끝 부분 위에 설치되는 경우 : (x > 0 and bar[x-1][y]) or bar[x][y]

- can_bar
1. 한쪽 끝 부분에 기둥이 있는 경우 : pillar[x][y-1] or pillar[x+1][y-1]
2. 양쪽 끝 부분이 다른 보와 동시에 연겨되는 경우 : (x > 0 bar[x-1][y]) and bar[x+1][y]

-remove_build
1. 일단 입력된 부분을 0으로 바꾸기
2. 한 부분이 바뀌면 영향을 미치는 부분은 총 6칸 : x - 1 < x < x + 2
ex) x = 3, y = 2인 경우 2 <= x <= 4, 2 <= y <= 3
3. pillar[x][y]가 1이고 can_pillar가 False일 경우는 제거하면 안됨
   pillar[x][y] = 1로 다시 변경
4. bar[x][y]가 1이고 can_bar가 False일 경우는 제거하면 안됨
   bar[x][y] = 1로 다시 변경
"""

pillar = []
bar = []

def solution(n, build_frame):
    answer = []
    
    global pillar, bar
    pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    bar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    for x, y, kind, cmd in build_frame:
        if kind == 0:
            if cmd == 1:
                if can_pillar(x, y):
                    pillar[x][y] = 1
            else:
                pillar[x][y] = 0
                if not remove_build(x, y):
                    pillar[x][y] = 1
        else:
            if cmd == 1:
                if can_bar(x, y):
                    bar[x][y] = 1
            else:
                bar[x][y] = 0
                if not remove_build(x, y):
                    bar[x][y] = 1
    
    for i in range(n+1):
        for j in range(n+1):
            if pillar[i][j]:
                answer.append([i, j, 0])
            if bar[i][j]:
                answer.append([i, j, 1])
    
    return answer

## 기둥을 설치해도 되는 지 확인하는 함수
def can_pillar(x, y):
    if y == 0 or pillar[x][y-1]:
        return True
    if (x > 0 and bar[x-1][y]) or bar[x][y]:
        return True
    
    return False

## 바를 설치해도 되는 지 확인하는 함수
def can_bar(x, y):
    if pillar[x][y-1] or pillar[x+1][y-1]:
        return True
    if x > 0 and bar[x-1][y] and bar[x+1][y]:
        return True
    
    return False

## 제거해도 되는 지 확인하는 함수
def remove_build(x, y):
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if pillar[i][j] and can_pillar(i, j) == False:
                return False
            if bar[i][j] and can_bar(i, j) == False:
                return False
    return True