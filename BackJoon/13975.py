import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  n = int(input())
  answer = 0
  
  chapter = list(map(int, input().split()))
  heapq.heapify(chapter) 

  while len(chapter) != 1:
    tmp = heapq.heappop(chapter) + heapq.heappop(chapter)
    answer += tmp
    heapq.heappush(chapter, tmp)
  
  print(answer)