"""
1. head, number, tail 부분 나눌 p 만들기
- r'([a-zA-Z\-.\s]+)([0-9]{0,5})(.*)'
1) head 부분에는 숫자가 들어갈 수 없음
2) number 부분에는 숫자가 5자리까지 들어갈 수 있음
3) tail 부분은 number 뒷부분

2. for문을 돌리면서 p 기준에 맞는 거 찾기
ex) img12.png -> (img, 12, .png) 이렇게 변환됨

3. tmp에 p 기준으로 나눈 거 저장
※ append 대신에 extend 사용한 이유
- append 사용 시 tmp : [[(img, 12, .png)], [(img, 12, .png)]]
- extend 사용 시 tmp : [(img, 12, .png), (img, 12, .png)]

4. tmp를 정렬
1) head 사전순
2) number 크기 순
3) tail 입력받은 순

5. tmp를 요소를 합친 걸 answer에 저장
"""

import re

def solution(files):
    answer = []
    tmp = []
    p = re.compile(r'([a-zA-Z\-.\s]+)([0-9]{0,5})(.*)')

    for file in files:
        tmp.extend(p.findall(file))

    tmp.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for file in tmp:
        answer.append("".join(file))

    return answer