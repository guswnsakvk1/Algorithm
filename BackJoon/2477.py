"""
규칙
1. 변이 1개만 있는 곳에서 시계반대방향으로 돌면
2. 처음으로 변이 2개가 되는 곳은 2번째로 입력받는 값과
   다음으로 변이 2개가 되는 곳은 1번째로 입력받는 값을 곱한 거에
3. 최대 넓이에 빼고 k를 곱하면 됨
"""

from collections import deque

k = int(input())

queue = deque([])
num = 0
cnt = {1:0, 2:0, 3:0, 4:0}
bulid = {1 : [], 2 : [], 3 : [], 4 : []}

for _ in range(6):
  direction, length = map(int, input().split())
  queue.append((direction, length))
  cnt[direction] += 1

for i in range(4):
  if cnt[i+1] == 1:
    num = i+1
    break

while queue:
  direction, length = queue.popleft()
  if direction == num:
    bulid[direction].append(length)
    break
  else:
    queue.append((direction, length))

width = 0
height = 0

while queue:
  direction, length = queue.popleft()
  bulid[direction].append(length)

  if len(bulid[direction]) == 2:
    if width == 0:
      width = length
    else:
      height = bulid[direction][0]

max_width = sum(bulid[1])
max_height = sum(bulid[3])

print((max_height * max_width - height * width) * k)