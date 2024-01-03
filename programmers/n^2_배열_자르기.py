## 문제의 범위가 10 ** 7까지이므로 이중 for문 쓰고
## 배열을 만들고 배열을 자르면 시간초과
## 따라서 내가 원하는 범위의 값만 배열에 저장하는 것이 포인트
## y와 x의 좌표는 어떤 n값이 주어지느냐에 따라 달라짐
## y는 i // n
## x는 i % n

def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        y = i // n + 1
        x = i % n + 1
        answer.append(max(x, y))
    
    return answer