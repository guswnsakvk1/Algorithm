def solution(s):
    answer = []
    ## 처음과 끝에 있는 괄호삭제
    s = s[1:-1]
    ## {는 나눌 때 필요없으므로 삭제
    s = s.replace('{', '')
    ## },을 기준으로 lst를 나누기
    lst = s.split('},')
    ## 맨 마지막에 있는 } 없애기
    lst[-1] = lst[-1][:-1]
    ## lst안에 있는 str의 길이 순으로 정렬
    lst.sort(key=len)
    
    for i in lst:
        ## i는 str이기에
        ## 10이상 넘어가는 숫자를 남기위한 num
        num = ''
        for j in range(len(i)):
            if i[j] != ',':
                num += i[j]
            else:
                ## num이 answer에 없으면 answer에 추가
                if int(num) not in answer:
                    answer.append(int(num))
                num = ''
            
            ## answer에 들어갈 숫자가 마지막에 있을 경우
            if j == len(i) - 1 and int(num) not in answer:
                answer.append(int(num))
    
    return answer