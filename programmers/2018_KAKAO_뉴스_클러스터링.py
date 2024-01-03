"""
입력 형식
1. str1과 str2의 두 문자열이 들어온다
2. 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다.
   이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가
   들어있을 경우는 그 글자 쌍을 버린다.
3. 다중집합 우너소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다.

해결방법
1. 입력받은 str1과 str2를 모두 소문자 또는 대문자로 변경
2. re 라이브러리를 사용해서 영문자로만 이루어진 글자 쌍과 개수를 딕셔너리에 저장
3. re 라이브러리로 구한 딕셔너리를 사용해서 교집합, 합집합 구하기
1) 교집합 겹치는 글자 쌍의 개수가 작은 것을 따라감
2) 합집합 겹치는 글자 쌍의 개수가 많은 것을 따라감
4. 교집합 / 합집합 * 65536 소수점 버림 출력
"""


import math
import re

def solution(str1, str2):
    p = re.compile('[a-z]+')
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_dic = {}
    str2_dic = {}
    
    for i in range(len(str1)-1):
        m = p.search(str1[i:i+2])
        if m == None or m.start() == 1 or m.end() == 1:
            continue

        try:
            str1_dic[str1[i:i+2]] += 1
        except:
            str1_dic[str1[i:i+2]] = 1 

    for i in range(len(str2)-1):
        m = p.search(str2[i:i+2])
        if m == None or m.start() == 1 or m.end() == 1:
            continue

        try:
            str2_dic[str2[i:i+2]] += 1
        except:
            str2_dic[str2[i:i+2]] = 1
    
    union = {}
    intersection = {}
    
    for key, value in str1_dic.items():
        if key in str2_dic:
            intersection[key] = min(value, str2_dic[key])
    
    for key, value in str1_dic.items():
        if key in str2_dic:
            union[key] = max(value, str2_dic[key])
        else:
            union[key] = value
            
    for key, value in str2_dic.items():
        if key not in str1_dic:
            union[key] = value
    
    return math.floor(sum(intersection.values()) / sum(union.values()) * 65536) if len(union) != 0 else 65536