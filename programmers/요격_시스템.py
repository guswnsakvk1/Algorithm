"""

입력된 target이 겹치는 부분을 활용해서 정답을 구하는 방법을 사용함
end가 현재 target의 시작부분보다 크다면 겹치는 부분이 있는 것이므로
end를 end와 target의 끝부분 중 작은 것으로 바꾸기

만약 end가 현재 target의 시작부분보다 작다면 겹치는 부분이 없는 것이므로
answer에 1더하고 end를 target의 끝부분으로 바꾸기

"""

def solution(targets):
    answer = 1
    
    targets.sort(key=lambda x:(x[0], x[1]))
    end = targets[0][1]
    
    for i in range(1, len(targets)):            
        if end > targets[i][0]:
            end = min(end, targets[i][1])
        else:
            answer += 1
            end = targets[i][1]
    
    return answer