"""
1. 시작하는 시간, 끝나는 시간으로 정렬한다.
2. 끝나는 시간을 저장하는 리스트 end_tiems
3. end_times가 비어있으면 끝나는 시간 넣기
4. end_times가 있으면
   시작 시간보다 end_times에 있는 값보다 크거나 같은 값 모두 삭제
"""

import heapq
import sys
input = sys.stdin.readline

n = int(input())
answer = 0

h = []
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(h, (start, end))

end_times = []
while h:
    start, end = heapq.heappop(h)

    while end_times:
        if start >= end_times[0]:
            heapq.heappop(end_times)
        else:
            break
    
    heapq.heappush(end_times, end)
    answer = max(answer, len(end_times))

print(answer)