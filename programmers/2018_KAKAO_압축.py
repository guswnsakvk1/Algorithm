"""
1. 일파벳 순서대로 있는 딕셔너리 만들기

2. new_alpha에 들어있는 글자들이 msg의 맨 앞에 있는 지 확인
1) 있다면 answer에 value 저장
2) 없다면 alpha에서 value 찾아서 저장

3. 현재 word에서 다음 글자를 합한 str을 new_alpha에 순서와 함께 저장

4. msg가 없어질 때 까지 반복
"""

from string import ascii_uppercase

def solution(msg):
    answer = []
    alpha = {}
    new_alpha = {}
    
    cnt = 27
    for i in range(len(ascii_uppercase)):
        alpha[ascii_uppercase[i]] = i + 1
    
    while msg:
        check = False
        word = ''
        for i in sorted(new_alpha.items(), key = lambda x : x[1], reverse = True):
            if msg.find(i[0]) == 0:
                answer.append(i[1])
                check = True
                word = i[0]
                break
                
        if not check:
            answer.append(alpha[msg[0]])
            word = msg[0]
        
        word_len = len(word)
        
        new_alpha[msg[:word_len+1]] = cnt
        cnt += 1
        msg = msg[word_len:]
    
    return answer