import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
d = deque(i for i in range(1, n+1))

answer = 0

for i in position:
  while True:
    if d[0] == i:
      d.popleft()
      break
    else:
      if d.index(i) < len(d)/2:
        while d[0] != i:
          d.append(d.popleft())
          answer += 1
      else:
        while d[0] != i:
          d.appendleft(d.pop())
          answer += 1

print(answer)