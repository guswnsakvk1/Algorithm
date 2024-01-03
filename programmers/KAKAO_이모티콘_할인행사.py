import itertools
import math

def solution(users, emoticons):
    answer = [(0, 0)]

    max_sale = 10
    min_sale = 40
    ## 최대할인, 최소할인 
    for i, j in users:
        num = math.ceil((i / 10)) * 10
        max_sale = max(max_sale, num)
        min_sale = min(min_sale, num)
    
    print(min_sale, max_sale)
    
    ## 할인가능한 모든 경우의 수 구하기
    sale = [i for i in range(min_sale, max_sale+1, 10)]
    sale_case = itertools.product(sale, repeat=len(emoticons))
    
    print(sale)
    print(list(sale_case))

    ## 모든 할인율 케이스 확인
    for case in sale_case:
        ## 구독형 서비스 새로 가입하는 회원 수
        new = 0
        ## 이익
        profit = 0
        for user in users:
            ## 유저가 내야하는 비용
            user_cost = 0
            for i in range(len(emoticons)):
                ## 이모티콘 할인율이 유저가 원하는 할인율을 넘을 경우
                if user[0] <= case[i]:
                    ## 유저 비용에 추가
                    user_cost += emoticons[i] * ((100 - case[i]) / 100)
            
            ## 유저가 내야하는 비용이 유저가 생각하는 비용보다 클 경우
            if user_cost >= user[1]:
                ## 구독서비스 가입
                new += 1
            else:
                ## 아니면 이익에 추가
                profit += user_cost
        
        ## 만약 answer[0]이 new보다 크면
        ## 무조건 answer[0], answer[1]은
        ## new와 profit으로 변경
        if answer[0] < new:
            answer[0] = new
            answer[1] = profit
        ## 만약 answer[0]은 같은데
        ## answer[1]이 profit보다 작으면
        ## answer[1]은 profit으로 변경
        elif answer[0] == new and answer[1] < profit:
            answer[1] = profit