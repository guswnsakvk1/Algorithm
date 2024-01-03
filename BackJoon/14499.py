"""
주사위는 맞은편의 합이 7을 사용해서 
주사위를 이동했을 때 dice의 주사위 전개도 구하기
"""

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
dice = [[0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))

for cmd in cmds:
  x += dx[cmd]
  y += dy[cmd]

  if x < 0 or x >= n or y < 0 or y >= m:
    x -= dx[cmd]
    y -= dy[cmd]
    continue

  if cmd == 1:
    dice[1][2] = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] = 7 - dice[1][2]
    dice[3][1] = 7 - dice[1][1]
  elif cmd == 2:
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] = 7 - dice[1][0]
    dice[3][1] = 7 - dice[1][1]
  elif cmd == 3:
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] = dice[3][1]
    dice[3][1] = 7 - dice[1][1]
  elif cmd == 4:
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = 7 - dice[2][1]

  if graph[x][y] != 0:
    nums[dice[3][1]] = graph[x][y]
    graph[x][y] = 0
  else:
    graph[x][y] = nums[dice[3][1]]

  print(nums[dice[1][1]])