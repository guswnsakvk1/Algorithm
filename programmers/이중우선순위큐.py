import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for op in operations:
        if op == 'D 1':
            if max_heap:
                num = heapq.heappop(max_heap)
                min_heap.remove(-num)
        elif op == 'D -1':
            if min_heap:
                num = heapq.heappop(min_heap)
                max_heap.remove(-num)
        else:
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
    
    if min_heap and max_heap:
        answer.append(heapq.heappop(max_heap)*-1)
        answer.append(heapq.heappop(min_heap))
        return answer
    else:
        return [0,0]