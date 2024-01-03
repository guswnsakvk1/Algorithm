"""
1. 광물의 개수에 따른 필요한 곡괭이 갯수 구하기
1) 5로 나누어 떨어질 경우는 len(minerals) // 5
2) 5로 나누어 떨어지지 않는 경우는 len(minerals) // 5 + 1

2. 필요한 곡괭이 갯수만큼 가장 좋은 곡괭이 고르기

3. 순열을 사용해서 곡괭이를 사용하는 순서의 모든 경우의 수 구하기
1) permutations 사용

4. 모든 경우의 수마다 피로도를 구하기
"""


from itertools import permutations

def solution(picks, minerals):
    pickaxs = []
    answer = 1e9
    
    need_pick = len(minerals) // 5 if len(minerals) % 5 == 0 else len(minerals) // 5 + 1
    
    for i in range(3):
        if need_pick != 0:
            if picks[i] > need_pick:
                pickaxs.extend([i] * need_pick)
            else:
                pickaxs.extend([i] * picks[i])
            need_pick -= picks[i]
        else:
            break
    
    pickax = permutations(pickaxs, len(pickaxs))
    
    for pick in set(pickax):
        fatigue = 0
        cnt = 0
        l = 0
        for miner in minerals:
            try:
                if pick[l] == 0:
                    fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
                elif pick[l] == 1:
                    if miner == "diamond":
                        fatigue += 5
                    else:
                        fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
                else:
                    if miner == "diamond":
                        fatigue += 25
                    elif miner == "iron":
                        fatigue += 5
                    else:
                        fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
            except:
                break
            
        answer = min(answer, fatigue)
    
    return answer