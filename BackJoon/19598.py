import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
lst = []
for _ in range(n):
    start, end = map(int, input().split())
    lst.append((start, end))

lst.sort()

answer = 0

for start, end in lst:
    if not heap:
        heapq.heappush(heap, end)
        answer = max(answer, 1)
    else:
        while heap:
            tmp = heapq.heappop(heap)
            
            if start < tmp:
                heapq.heappush(heap, tmp)
                heapq.heappush(heap, end)
                break
            else:
                continue
        
        if not heap:
            heapq.heappush(heap, end)
        
        answer = max(answer, len(heap))

print(answer)