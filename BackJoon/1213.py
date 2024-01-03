"""
1. 입력받은 문자열을 리스트(word)로 만들고 사전순으로 정렬하기

2. 리스트에 각각 문자가 몇개 있는 지 obj(counter)로 만들기

3. obj(counter) 요소에 (value // 2) * 2 빼기

4. answer에 key의 (value // 2) 곱해서 추가
※ 앞으로 읽으나 뒤로 읽으나 같은 문자열을 만드는 것이므로
   answer에는 * 2 안함

5. obj(counter) value가 0이 아닌 값이 있다면 cnt에 더하고
   place에 key값 추가

6. 만약 cnt가
   1) 1이면 answer + place[0] + answer[::-1]
   2) 0이면 answer + answer[::-1]
   3) 아니면 I'm Sorry Hansoo 출력
"""

from collections import Counter

answer = ''

word = list(input())
word.sort()
counter = Counter(word)

for i in counter:
    answer +=  i * (counter[i] // 2)
    counter[i] -= (counter[i] // 2) * 2

cnt = 0
place = []

for i in counter:
  if counter[i] != 0:
    cnt += counter[i]
    place.append(i)

if cnt == 1:
  print(answer + place[0] + answer[::-1])
elif cnt == 0:
  print(answer + answer[::-1])
else:
  print("I'm Sorry Hansoo")