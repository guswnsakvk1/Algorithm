## 최소값을 구하려면 맨 뒤에서부터 배달, 수거를 진행

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    ## 배달할 거 저장하는 변수
    d = 0
    ## 픽업할 거 저장하는 변수
    p = 0
    
    for i in range(n-1, -1, -1):
        ## 현재 집 배달할 개수 빼기
        d -= deliveries[i]
        ## 현재 집 수거할 개수 빼기
        p -= pickups[i]
        ## 현재 집을 몇 번이나 왔다갔다 해야하는 지 저장하는 변수
        cnt = 0
        
        ## 배달, 수거할 개수가 0보다 작으면 다시 왔다갔다 해야하므로
        ## d와 p가 둘 중 하나라도 0이라면
        while d < 0 or p < 0:
            ## d에 cap 더하기
            d += cap
            ## p에 cap 더하기
            p += cap
            cnt += 1
        
        ## 물류창고와 집 사이 거리는 i + 1
        ## 왕복 거리 (i + 1) * 2
        ## cnt 만큼 왕복해야하니 
        ## answer에 (((i + 1) * 2) * cnt) 더하기
        answer += (((i + 1) * 2) * cnt)
    
    return answer