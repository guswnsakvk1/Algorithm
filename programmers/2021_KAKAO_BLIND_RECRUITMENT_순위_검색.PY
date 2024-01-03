import itertools

def solution(info, query):
    answer = []
    applicants = {}

    ## 지원자들 스팩에 해당하는 모든 경우의 수 만들기
    ## 개발언어, 직군, 경력, 소울푸드 총 2**4 개의 가지
    ## 개발언어, 직군, 경력, 소울푸드 : 지원자 점수 <- 형태로 만들어서 저장
    for i in info:
        lst = i.split()
        score = int(lst[-1])
        for j in range(5):
            for c in itertools.combinations(lst[:-1], j):
                key = "".join(c)
                if key in applicants:
                    applicants[key].append(score)
                else:
                    applicants[key] = [score]

    ## 이분탐색을 사용하기 위해 sort사용      
    for key in applicants.keys():
        applicants[key].sort()
        
    for q in query:
        ## '-'는 해당 조건을 고려하지 않기에 삭제
        ## '-' 때문에 조합을 사용해서 지원자 스팩의 모든 경우의 수를 저장한 것
        lst = q.replace("and", "").replace("-", "").split()
        key = "".join(lst[:-1])
        score = int(lst[-1])

        ## 요구하는 스팩이 없을 경우 answer에 0을 넣는 코드
        if key in applicants:
            temp = applicants[key]
        else:
            answer.append(0)
            continue
        left = 0
        right = len(temp)

        while left < right:
            mid = (left + right) // 2
            if temp[mid] >= score:
                right = mid
            else:
                ## 0부터 수를 새기에 +1을 해주는 것
                left = mid + 1

        answer.append(len(temp) - left)
        
    return answer