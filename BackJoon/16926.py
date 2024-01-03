from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

up_down = N
left_right = M

start = 0
x_end = M-1
y_end = N-1

tmp = []

while up_down > 0 and left_right > 0:
  queue = deque([])

  for i in range(left_right-1):
    queue.append(lst[start][start+i])

  for i in range(up_down-1):
    queue.append(lst[start+i][x_end])

  for i in range(left_right-1):
    queue.append(lst[y_end][x_end-i])

  for i in range(up_down-1):
    queue.append(lst[y_end-i][start])

  tmp.append(queue)
  start += 1
  x_end -= 1
  y_end -= 1
  up_down-= 2
  left_right-= 2

for _ in range(R):
  for queue in tmp:
    queue.append(queue.popleft())

up_down = N
left_right = M

start = 0
x_end = M-1
y_end = N-1

for t in tmp:
  n = 0
  for i in range(left_right-1):
    lst[start][start+i] = t[n]
    n += 1

  for i in range(up_down-1):
    lst[start+i][x_end] = t[n]
    n += 1

  for i in range(left_right-1):
    lst[y_end][x_end-i] = t[n]
    n += 1

  for i in range(up_down-1):
    lst[y_end-i][start] = t[n]
    n += 1

  start += 1
  x_end -= 1
  y_end -= 1
  up_down-= 2
  left_right-= 2

for l in lst:
  print(*l)