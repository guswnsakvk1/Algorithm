import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int,input().split())) for _ in range(n)]

arr = []
for x, y in points:
    arr.append((x, 1))
    arr.append((y, -1))

arr.sort(key=lambda x: (x[0], x[1]))

cnt = 0
ans = 0
for x, v in arr:
    cnt += v
    ans = max(ans, cnt)

print(ans)

## heap 풀이
import heapq
import sys
input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))

lines.sort(key=lambda x : x[0])

heap = []
heapq.heappush(heap, lines[0][1])

answer = 1

for s, e in lines[1:]:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    answer = max(answer, len(heap))

print(answer)