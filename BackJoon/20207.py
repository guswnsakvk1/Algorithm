import sys
input = sys.stdin.readline

def set_height(height, s, e):
  for i in range(s, e+1):
    height[i] += 1

N = int(input())

date = [tuple(map(int, input().split())) for _ in range(N)]

date.sort()

start, end = date[0][0], date[0][1]
height = [0] * 366
set_height(height, start, end)
answer = 0

for s, e in date[1:]:
  if start <= s <= end:
    set_height(height, s, e)
    end = max(end, e)
  elif s == end + 1:
    end = e
  else:
    max_height = max(height[start:end + 1])
    answer += (end - start + 1) * max_height
    start = s
    end = e
    set_height(height, s, e)

max_height = max(height[start:end + 1])
answer += (end - start + 1) * max_height
print(answer)