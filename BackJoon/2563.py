"""
1. 좌표를 입력받고 그 중 가장 큰 x, y 좌표를 구한다

2. 가장 큰 x, y에 각각 10을 더하고 2차 배열을 만든다
※ 색종이의 크기가 가로, 세로가 10이기 때문

3. 입력받은 좌표 x, y로 이중 for문을 돌려서 색종이가 있는 위치에 1로 변경

4. 2차 배열에 1의 개수를 구해서 return 해주기
"""

n = int(input())

coordinate_list = []
max_x = 0
max_y = 0

for i in range(n):
    a, b = map(int, input().split())
    coordinate_list.append((a, b))
    if max_x < a:
        max_x = a
    if max_y < b:
        max_y = b

paper = [[0 for _ in range(max_y + 10)] for _ in range(max_x + 10)]

for x, y in coordinate_list:
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

answer = 0

for i in paper:
    answer += i.count(1)

print(answer) 