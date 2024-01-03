"""
1. Counter를 사용해서 입력받은 값을 딕셔너리로 만들기

2. 6은 9를 뒤집어서 이용하능하고 9는 6을 뒤집어서 사용가능
   6이랑 9를 처리하기
1) 만약 9가 있다면
- 6도 있다면 numbers['6']에 numbers['9']더하기
- 6이 없다면 numbers['6']을 numbers['9']로 초기화
- six를 (numbers['6'] // 2) + (numbers['6'] % 2)로 업데이트
2) 만약 6이 있다면
- six를 (numbers['6'] // 2) + (numbers['6'] % 2)로 업데이트
※ 6만 있는 경우, 9만 있는 경우, 6이랑 9가 둘 다 있는 경우를 나눠준 것

3. numbers 딕셔너리에서 6이랑 9삭제

4. 만약 numbers에 
1) 값이 있다면
- numbers에서 가장 큰 값을 구하고
- six와 비교해서 더 큰 값 출력
2) 값이 없다면
- six 출력

"""

from collections import Counter

n = input()

numbers = Counter(n)
six = 0

if '9' in numbers:
    try:
        numbers['6'] += numbers['9']
    except:
        numbers['6'] = numbers['9']
    
    six = (numbers['6'] // 2) + (numbers['6'] % 2)
elif '6' in numbers:
    six = (numbers['6'] // 2) + (numbers['6'] % 2)

del numbers['9'], numbers['6']

if numbers:
    max_num = max(numbers.values())
    print(max(max_num, six))
else:
    print(six)