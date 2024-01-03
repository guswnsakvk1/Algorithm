## 입실 시간과 퇴실 시간을 숫자로 변화하여 배열만들기
## heap을 사용하는 이유: 퇴실시간 중 가장 작은 값만 비교하면 되기 때문

import heapq

def solution(book_time):
    answer = 1
    heap = []
    book_time_list = [(int(time[0][:2]) * 60 + int(time[0][3:]), int(time[1][:2]) * 60 + int(time[1][3:])) for time in book_time]
    book_time_list.sort()
    
    for start, end in book_time_list:
        if not heap:
            heapq.heappush(heap, end+10)
            continue
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, end+10)
    return answer