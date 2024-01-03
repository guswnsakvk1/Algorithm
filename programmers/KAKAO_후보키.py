from itertools import combinations

def solution(relation):
    ## 가로 길이
    row = len(relation)
    ## 세로 길이
    col = len(relation[0])
    
    ## 모든 조합을 넣을 리스트
    candidates = []
    ## 1부터 col까지 모든 조합 구하기
    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))
    
    ## 유일성을 저장하는 리스트
    unique = []
    ## 가능한 모든 조합 만큼 for문 돌림
    for candidate in candidates:
        ## tmp는 만들 수 있는 모든 조합을 임시 저장하는 리스트
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        ## tmp를 set한 길이가 row과 같다면 unique에 저장
        ## set을 하는 이유는 중복을 없애기 위해 사용
        if len(set(tmp)) == row:
            unique.append(candidate)
    
    ## 최소성을 저장하는 리스트
    answer = set(unique)
    for i in range(len(unique) - 1):
        for j in range(i + 1, len(unique)):
            ## 만약 unique[i]의 길이와 len(set(unique[i]) & set(unique[j]))가 같으면 최소성을 만족하는 것이 아니기에 삭제
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                ## remove대신 discard를 쓰는 이유
                ## discard는 지우려는 값이 없더라도 에러를 발생하지 않기에 사용
                answer.discard(unique[j])
    
    return len(answer)