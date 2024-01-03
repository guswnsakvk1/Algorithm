def solution(priorities, location):
    answer = 0
    while(True):
        num = max(priorities)
        for i in range(len(priorities)):
            if(num == priorities[i]):
                answer += 1
                priorities[i] = 0
                num = max(priorities)
                if(i == location):
                    return answer