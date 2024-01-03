from collections import deque

a = int(input())

for i in range(a):
  n, m = map(int, input().split())
  queue = deque(map(int, input().split()))
  max_num = max(queue)
  answer = 1

  while queue:
    num = queue.popleft()
    if m == 0:
      if num == max_num:
        print(answer)
        break
      else:
        m = len(queue)
        queue.append(num)
    else:
      m -= 1
      if num == max_num:
        max_num = max(queue)
        answer += 1
      else:
        queue.append(num)