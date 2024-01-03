## [1,1,1,1], 3이 입력되면 아래와 같이 방법으로 3을 만들 수 있음
## -1+1+1+1+1 = 3
## +1-1+1+1+1 = 3
## +1+1-1+1+1 = 3
## +1+1+1-1+1 = 3
## +1+1+1+1-1 = 3
## bfs로 만들 수 있는 방법을 찾을 꺼임

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(numbers[0], 1), (-numbers[0], 1)])
    
    while queue:
        num, idx = queue.popleft()
        if idx == len(numbers):
            break
            
        num1 = num + numbers[idx]
        num2 = num - numbers[idx]
        
        if num1 == target and idx == len(numbers)-1:
            answer += 1
        if num2 == target and idx == len(numbers)-1:
            answer += 1
            
        queue.append((num1, idx+1))
        queue.append((num2, idx+1))
    
    return answer
