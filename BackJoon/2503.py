"""
1. 만들 수 있는 모든 세 자리 수를 저장한 배열을 만든다.
2. 입력받은 숫자들이랑 모든 경우의 수를 비교하면서
   각각 입력받은 숫자들의 strike, ball의 개수가 모두 다 같다면
   answer에 1더하기
"""

import sys
input = sys.stdin.readline

answer = 0
n = int(input())

conjectures = []
for i in range(n):
  conjectures.append(tuple(input().split()))

numbers = []

for i in range(1, 10):
  for j in range(1, 10):
    for k in range(1, 10):
      if i != j and i != k and j != k:
        numbers.append((str(i), str(j), str(k), 0, 0))

for number in numbers:
  one, two, three, strike, ball = number
  check = False
  for conjecture in conjectures:
    num, strike_num, ball_num = conjecture
    
    if one == num[0]:
      strike += 1
    elif one in num:
      ball += 1

    if two == num[1]:
      strike += 1
    elif two in num:
      ball += 1

    if three == num[2]:
      strike += 1
    elif three in num:
      ball += 1
    
    if strike == int(strike_num) and ball == int(ball_num):
      strike = 0
      ball = 0
    else:
      check = True
      break

  if not check:
    answer += 1

print(answer)