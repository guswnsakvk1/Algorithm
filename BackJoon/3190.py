"""
규칙
1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 
   즉, 몸길이는 변하지 않는다.

1. 벽이나 자기자신의 몸에 부딪힐 때 가지 계속 진행한다.
2. 만약 cmd_x가 answer와 같다면 cmd_d를 보고 방향을 바꾼다.
3. nx, ny라는 앞으로 전진한 좌표를 변수로 저장
4. 만약 nx, ny가 범위를 넘어가거나 자기자신과 부딪히면 종료
5. 아니면 (nx, ny)를 queue에 넣고 answer에 +1
6. 만약 (nx, ny)가 apple에 있다면 apple에 (nx, ny) 삭제
   없다면 queue에서 popleft()

apple : 사과의 좌표를 저장하는 리스트
cmd : x초후 c로 바꿀 방향을 저장하는 deque
queue : 뱀의 좌표를 저장하는 deque
d : 뱀의 방향
dx, dy : 동서남북 좌표를 나타내는 리스트
"""

from collections import deque
import sys
inpurt = sys.stdin.readline

N = int(input())

apple = []
K = int(input())

for _ in range(K):
  x, y = map(int,input().split())
  apple.append((x-1, y-1))

cmd = deque([])
L = int(input())

for _ in range(L):
  x, c = input().split()
  cmd.append((x, c))

cmd_x, cmd_d = cmd.popleft()

queue = deque([(0,0)])

d = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = 0

while True:
  x, y = queue[-1]

  if answer == int(cmd_x):
    if cmd_d == 'L':
      if d != 0:
        d -= 1
      else:
        d = 3
    else:
      if d != 3:
        d += 1
      else:
        d = 0

    if cmd:
      cmd_x, cmd_d = cmd.popleft()
  
  nx = x + dx[d]
  ny = y + dy[d]

  if nx < 0 or nx >= N or ny < 0 or ny >= N:
    break

  if (nx, ny) in queue:
    break

  queue.append((nx, ny))
  answer += 1

  if (nx, ny) in apple:
    apple.remove((nx, ny))
  else:
    queue.popleft()

print(answer+1)