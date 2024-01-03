"""
1. 금메달, 은메달, 동메달의 개수 순서대로 정렬
2. for문을 N-1까지 돌린다
3. i번째와 i+1번째의 메달 개수를 비교해서 다르면
   answer에 cnt 더하기
4. 같으면 cnt에 1 더하기

cnt : 똑같은 메달을 가진 나라가 몇개나 있는지 확인하는 변수
"""

import sys
inpurt = sys.stdin.readline

answer = 1
cnt = 1
check = False
N, K = map(int, input().split())

olympics = []
for _ in range(N):
  olympics.append(tuple(map(int, input().split())))

olympics.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N-1):
  a_num, a_gold, a_silver, a_bronze = olympics[i]
  b_num, b_gold, b_silver, b_bronze = olympics[i+1]

  if a_num == K:
    check = True
    print(answer)
    break
  
  if a_gold != b_gold or a_silver != b_silver or a_bronze != b_bronze:
    answer += cnt
    cnt = 1
  else:
    cnt += 1

if not check:
  print(answer)