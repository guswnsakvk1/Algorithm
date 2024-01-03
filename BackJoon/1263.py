import sys
input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x:-x[1])
sleep = lst[0][1] - lst[0][0]

for required_time, dead_line in lst[1:]:
  if sleep > dead_line:
    sleep = dead_line

  sleep -= required_time

if sleep < 0:
  print(-1)
else:
  print(sleep)