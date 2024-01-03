## dict을 사용해서 중복된 것이 있는 지 확인
## 중복을 확인하는 이유: 모든 것을 확인하고 돌리면 느림
## 

def solution(weights):
    answer = 0
    
    ## weights를 담는 dict 
    w_dic = dict()

    ## dict 만들기
    for w in weights:
        if w in w_dic:
            w_dic[w] += 1
        else:
            w_dic[w] = 1
    
    ## dict key값을 사용해서 list 만들기
    w_lst = list(w_dic.keys())
    
    for i in range(len(w_lst)):
        for j in range(i, len(w_lst)):
            w1, w2 = w_lst[i], w_lst[j]
            ## 같은 숫자가 2개 이상일 경우
            ## n(n-1) / 2 를 사용해서 answer에 더하기
            if i == j and w_dic[w1] > 1:
                answer += w_dic[w1] * (w_dic[w1] - 1) / 2
                continue
            
            ## 모든 케이스 확인
            if w1 * 2 == w2 * 3:
                answer += w_dic[w1] * w_dic[w2]
            if w1 * 2 == w2 * 4:
                answer += w_dic[w1] * w_dic[w2]
            if w1 * 3 == w2 * 2:
                answer += w_dic[w1] * w_dic[w2]
            if w1 * 3 == w2 * 4:
                answer += w_dic[w1] * w_dic[w2]
            if w1 * 4 == w2 * 2:
                answer += w_dic[w1] * w_dic[w2]
            if w1 * 4 == w2 * 3:
                answer += w_dic[w1] * w_dic[w2]
    
    return answer