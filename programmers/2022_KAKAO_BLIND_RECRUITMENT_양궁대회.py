from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    maxGap = -1e9
    results = list(combinations_with_replacement(range(0, 11), n))
    
    for result in results:
        info2 = [0] * 11
        lion, apeach = 0, 0
        
        for score in result:
            info2[10-score] += 1
            
        for score , (a, l) in enumerate(zip(info, info2)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += 10 - score
            else:
                lion += 10 - score
        
        if lion > apeach:
            gap = lion - apeach
            if maxGap < gap:
                maxGap = gap
                answer = info2
    
    return answer