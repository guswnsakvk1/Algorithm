import itertools

def solution(number):
    answer = 0
    nPr = itertools.combinations(number, 3)
    
    for i in list(nPr):
        if sum(i) == 0:
            answer += 1
    
    return answer