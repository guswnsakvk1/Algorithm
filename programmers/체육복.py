def solution(n, lost, reserve):
    newLost = list(set(lost) - set(reserve))
    newReserve = list(set(reserve) - set(lost))
    answer = n - len(newLost)
    for i in newLost:
        if i-1 in newReserve:
            answer += 1
            newReserve.remove(i-1)
            continue
        if i+1 in newReserve:
            answer += 1
            newReserve.remove(i+1)
            continue
    
    return answer