def solution(progresses, speeds):
    queue = []
    answer = []
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        queue.append(day)
    
    completion_day = queue[0]
    num = 0
    
    for i in queue:
        if completion_day >= i:
            num += 1
        else:
            answer.append(num)
            completion_day = i
            num = 1
            
    answer.append(num)
        
    return answer