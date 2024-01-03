## 1. 입력받은 n을 k진수로 변환하기
## 2. k진수로 바꾼 값을 0기준으로 나누기
## 3. 0으로 나눈 리스트의 값을 소수인지 확인
## split('0')으로 나누면 공백이 있는 상태가 나오므로
## if문에 len을 활용해서 공백 거르기

import math

def solution(n, k):
    answer = 0
    
    str_num = change(n, k)
    
    num_lst = str_num.split('0')

    for i in num_lst:
        if len(i) and check(int(i)):
            answer += 1
    
    return answer

def change(num, base):
    n = ''
    while num > 0:
        num, rest = divmod(num, base)
        n += str(rest)
        
    return n[::-1]

def check(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True