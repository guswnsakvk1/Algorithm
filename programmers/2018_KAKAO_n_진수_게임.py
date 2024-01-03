"""
1. N진수를 구한다.
2. N진수를 for문을 돌리면서 현재 내 차례일 경우 answer에 추가
3. 만약 len_answer가 p와 같으면 return answer
4. 아니면 계속 반복
"""

def solution(n, t, m, p):
    answer = ''
    num = 0
    cnt = 1
    len_answer = 0
        
    while True:
        n_binary = make_n_binary(num, n)
        for i in n_binary:
            if cnt == p:
                answer += i
                len_answer += 1
                
            if len_answer == t:
                return answer
            
            if cnt != m:
                cnt += 1
            else:
                cnt = 1
        num += 1

def make_n_binary(num, base):
    more_ten = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    
    if num == 0:
        return "0"
    
    n_binary_num = ''
    while num >= base:
        num, rest = divmod(num, base)
        if rest > 9:
            n_binary_num += more_ten[rest]
        else:
            n_binary_num += str(rest)
            
    if num != 0:
        if num > 9:
            n_binary_num += more_ten[num]
        else:
            n_binary_num += str(num)
            
    return n_binary_num[::-1]