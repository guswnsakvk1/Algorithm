"""
로봇 청소기 로짓
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
1) 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
2) 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
1) 반시계 반향으로 90도 회전한다.
2) 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
3) 1번으로 돌아간다
"""

import sys

inpurt = sys.stdin.readline

n, m = map(int, input().split())
r, c, direction = map(int, input().split())

lst = []

for _ in range(n):
  lst.append(list(map(int, input().split())))

answer = 0

direction_lst = [0] * 4
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
  if lst[r][c] == 0:
    lst[r][c] = 2
    answer += 1

  check = False

  for i in range(4):
    nx = r + dx[i]
    ny = c + dy[i]

    if lst[nx][ny] == 0:
      check = True
      break

  if not check:
    if direction % 2 == 0:
      direction = 2 if direction == 0 else 0
    else:
      direction = 3 if direction == 1 else 1
        
    if lst[r+dx[direction]][c+dy[direction]] != 1:
      r += dx[direction]
      c += dy[direction]
    else:
      break

    if direction % 2 == 0:
      direction = 2 if direction == 0 else 0
    else:
      direction = 3 if direction == 1 else 1
  else:
    if direction != 0:
      direction -= 1
    else:
      direction = 3

    if lst[r+dx[direction]][c+dy[direction]] == 0:
      r += dx[direction]
      c += dy[direction]

print(answer)