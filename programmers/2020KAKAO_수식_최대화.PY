"""
문제 풀 떄 드는 생각 정리

1. 주어진 문자열을 숫자와 기호로 분리하기
ex) 문자열 100-200*300-500+20
숫자 : [100,200,300,500,20]
기호 : [-,*,-,+]

2. +, -, *로 만들 수 있는 모든 경우의 수를 만들기

3. for문을 돌릴 때 임시 저장할 리스트를 만들어서 계산하기

문제 풀이 순서
1. 숫자와 기호가 있는 부분을 re라이브러리를 사용해서 나누기

2.  +, -, *로 만들 수 있는 모든 경우의 수 리스트 만들기

3. 우선순위가 높은 기호의 위치를 저장하기

4. eval을 사용해서 계산하기
"""

import re
import copy

def solution(expression):
    answer = 0
    
    pattern = '[*+-]'    
    nums = re.split(pattern, expression)
    
    symbols = re.findall(pattern, expression)
    
    symbol_seqs = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    
    for symbol_seq in symbol_seqs:
        tmp_num = copy.deepcopy(nums)
        tmp_symbol = copy.deepcopy(symbols)
        place_lst = []
        cnt = 0
        for symbol in symbol_seq:
            for place in range(len(tmp_symbol)):
                if symbol == tmp_symbol[place]:
                    place_lst.append(place - cnt)
                    cnt += 1
                    
            cnt = 0
            
            for place in place_lst:
                tmp_num[place] = str(eval(tmp_num[place] + symbol + tmp_num.pop(place+1)))
                tmp_symbol.pop(place)
                    
            place_lst.clear()
                
        answer = max(int(answer), abs(int(tmp_num[0])))
            
    return answer