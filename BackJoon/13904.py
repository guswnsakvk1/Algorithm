import heapq
import sys
input = sys.stdin.readline

N = int(input())

homework = {}
days = []
heap = []
answer = 0

for _ in range(N):
  d, w = map(int,(input().split()))
  try:
    homework[d].append(w)
  except:
    homework[d] = [w]

  if d not in days:
    days.append(d)

days.sort(reverse=True)

for i in range(days[0], 0, -1):
  if i in days:
    for hw in homework[i]:
      heapq.heappush(heap, -hw)

  if heap:
    answer -= heapq.heappop(heap)

print(answer)