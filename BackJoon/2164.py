from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])
cnt = 0

while len(queue) != 1:
  if cnt % 2 == 0:
    queue.popleft()
  else:
    queue.append(queue.popleft())
  cnt += 1

print(queue[0])