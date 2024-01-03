import math

def solution(k, d):
    answer = 0
    length = pow(d,2)
    
    for x in range(0, d+1, k):
        num = math.sqrt(length - pow(x, 2))
        answer += num // k + 1

    return answer