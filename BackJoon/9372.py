import heapq
import sys
input = sys.stdin.readline

def prim(graph, start):
  visited = set()
  min_heap = [(1,1)]
  mst = []

  while min_heap:
    node, weight = heapq.heappop(min_heap)
    if node not in visited:
      visited.add(node)
      mst.append((node, weight))

      for neighbor, neighbor_weight in graph[node]:
        if neighbor not in visited:
          heapq.heappush(min_heap, (neighbor, neighbor_weight))

  return mst
  
T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  
  graph = {i:[] for i in range(1, N+1)}

  for i in range(M):
    a, b = map(int, input().split())

    graph[a].append((b, 1))
    graph[b].append((a, 1))

  print(len(prim(graph, 1)) -1)