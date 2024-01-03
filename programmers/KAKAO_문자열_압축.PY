def solution(s):
    answer = len(s)
    ## 문자열 압축할 때 주어진 문자열 길이 절반까지반 확인하면 됨
    max_num = len(s) // 2
    
    for i in range(1, max_num + 1):
        ## n의 길이로 자른 문자열 저장하는 리스트
        divied_lst = []
        ## 자른 위치 저장하는 변수
        place = 0

        ## 현재 위치에 i를 더한 게 문자열 길이보다 작으면 실행
        while place + i <= len(s):
            divied_lst.append(s[place:place+i])
            place += i
        
        result = len(s)
        ## 문자열이 반복적으로 몇번 나왔는지 저장하는 변수
        cnt = 1
        ## 이전 문자열 저장하는 변수
        pre = divied_lst[0]
        for divied_str in divied_lst[1:]:
            ## 현재 문자열이 이전 문자열과 같으면
            ## cnt에 1더하기
            if divied_str == pre:
                cnt += 1
            ## 현재 문자열이 이전 문자열과 다르면
            else:
                ## 이전 문자열을 현재 문자열로 바꾸기
                pre = divied_str
                ## 만약 cnt가 1이면 계속 진행
                if cnt == 1:
                    continue
                ## 아니면 result에 압축되는 만큼 빼기
                else:
                    result += len(str(cnt)) - len(pre) * (cnt - 1)
                    cnt = 1
        
        ## 만약 cnt가 1보다 큰 경우
        ## 아직 안 뺀 것이 있는 거기 떄문에
        ## 한번 더 result에 압축되는 만큼 빼기
        if cnt > 1:
            result += len(str(cnt)) - len(pre) * (cnt - 1)

        answer = min(answer, result)
    
    return answer