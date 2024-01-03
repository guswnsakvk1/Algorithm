import sys
import heapq
input = sys.stdin.readline

V, E = map(int,input().split())
edge = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
  s,e,w = map(int, input().split())
  edge[s].append([w,e])
  edge[e].append([w,s])

answer = 0
cnt = 0
heap = [[0, 1]]

while heap:
  if cnt == V:
    break
    
  weight, node = heapq.heappop(heap)

  if not visited[node]:
    visited[node] = True
    cnt += 1
    answer += weight
    for i in edge[node]:
      heapq.heappush(heap, i)

print(answer)