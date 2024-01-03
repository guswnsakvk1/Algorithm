## num이 5일 경우는 앞자리 숫자를 5이상이면
## storey에 5를 더해준다
## 예시 입력: 95, 답: 6
## 95 -> 100 -> 0

def solution(storey):
    answer = 0
    while storey != 0:
        num = storey % 10
        
        if num <= 4:
            answer += num
        elif num == 5:
            answer += 5
            try:
                if int(str(storey)[-2]) > 4:
                    storey += 5
            except:
                print("예외가 발생했습니다")
        else:
            answer += (10 - num)
            storey += (10 - num)
        
        storey = storey // 10
        
    return answer