"""
캐시 저장방법
1. 캐시안에 원하는 값이 있다면 캐시안에 원하는 값을 삭제하고 새로 저장
2. 캐시안에 원하는 값이 없다면 캐시안에 제일 먼저 들어오 값을 제거하고 새로 값을 캐시에 저장

1. cache hit이면 answer 1증가
2. cache miss이면 answer 5증가
"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    queue_len = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            if city.lower() not in queue:
                if queue_len != cacheSize:
                    queue_len += 1
                else:
                    queue.popleft()
                answer += 5
            else:
                answer += 1
                queue.remove(city.lower())
            queue.append(city.lower())
    
    return answer