import collections

def solution(order):
    answer = 0
    stack = []
    queue = collections.deque(order)
    maxbox = len(order)
    check = False
    
    for i in range(1, maxbox+1):
        if queue[0] == i:
            answer += 1
            queue.popleft()
            check = True
            
        while stack:
            if queue[0] == stack[-1]:
                answer += 1
                queue.popleft()
                stack.pop()
            else:
                break
                
        if check:
            check = False
        else:
            stack.append(i)
    
    return answer