import heapq
import sys
input = sys.stdin.readline

N = int(input())

gas = []
for _ in range(N):
    a, b = map(int, input().split())
    gas.append((a,b))

gas.sort(key=lambda x:x[0])

L, P = map(int, input().split())
gas.append((L, 0))

heap = []
answer = 0
place = 0

for a,b in gas:
    P -= (a - place)
    place = a

    if P < 0:
      while P < 0 and heap:
          P -= heapq.heappop(heap)
          answer += 1
      
      if P < 0:
          print(-1)
          exit()

    heapq.heappush(heap, -b)

print(answer)