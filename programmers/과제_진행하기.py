"""
1. 과제는 순서대로 진행을 한다 -> plans를 시작하는 순서로 정렬하자
2. 현재 시간을 저장하는 변수(now_time), 각각 과제들의 남은 시간 저장하는 리스트(rest_times), answer에 저장하기 전 임시 저장 리스트 만들기(tmp)
3. for문을 돌릴 때 2번째 시작
4. for문의 plan의 시작 시간을 구해서 현재 시간과 차이를 구해서 시간 차이를 구한다(time_gap 변수). -> 시간의 차이만큼 앞에 다른 과제를 진행할 수 있기에 구함
5. rest_times가 있다면 앞에 과제를 진행한 것이 있기에
1) rest_times[-1]이 time_gap보다 작으면 그 과제는 다 끝낼 수 있기에 time_gap에 rest_times를 빼주고 answer에 tmp마지막의 값을 저장
2) rest_times[-1]이 time_gap보다 크면 그 과제는 다 끌낼 수 없기에 rest_times[-1]에 time_gap 빼주기
6. 현재 시간을 plan의 시작 시간으로 변경, tmp에 plan[0] 저장, rest_times plan[2] 저장
7. for문이 다 끝났는데 tmp가 남아있을 경우 뒤에서부터 answer에 저장
"""

def solution(plans):
    answer = []
    
    plans.sort(key=lambda x:x[1])
    
    start_hour, required_time = map(int, plans[0][1].split(':'))
    now_time = start_hour * 60 + required_time
    
    rest_times = [int(plans[0][2])]
    tmp = [plans[0][0]]
        
    for plan in plans[1:]:
        start_hour, required_time = map(int, plan[1].split(':'))
        time = start_hour * 60 + required_time
        
        time_gap = time - now_time
        
        while rest_times:
            if time_gap >= rest_times[-1]:
                time_gap -= rest_times.pop()
                answer.append(tmp.pop())
            else:
                rest_times[-1] -= time_gap
                break
                
        now_time = time
        tmp.append(plan[0])
        rest_times.append(int(plan[2]))
        
    for i in range(len(tmp)-1, -1, -1):
        answer.append(tmp[i])
    
    return answer