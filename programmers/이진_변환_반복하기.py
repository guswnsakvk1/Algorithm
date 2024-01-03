"""
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

1. x의 모든 0을 제거합니다.
2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.

예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

풀이
1. 이진수의 길이 구하기

2. 0의 개수 구하기

3. 이진수 길이에서 0의 개수 빼기

4. answer[0]에 +1, answer[1]에 + 0의 개수

5. 이진수 길이에서 0의 개수 뺀 게
1) 1이면 멈추기
2) 이진수 길이에서 0의 개수로 2진수 만들기

"""

def solution(s):
    answer = [0, 0]
    
    while True:
        bin_len = len(s)
        zero = s.count("0")
                
        bin_len -= zero
        
        answer[0] += 1
        answer[1] += zero
        
        if bin_len == 1:
            break
        else:
            tmp = bin(bin_len)[2:]
            s = tmp
            bin_len = len(s)
            
    
    return answer