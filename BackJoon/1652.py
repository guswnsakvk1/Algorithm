'''
1. 가로 한줄, 세로 한줄을 변수에 저장한다.
2. 저장한 변수를 'X'를 기준으로 split한다.
3. 리스트 안에 있는 문자열의 길이가 2가 넘어가면 answer에 +1 한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
answer_x = 0
answer_y = 0

room = []
for _ in range(n):
  room.append(list(input().rstrip()))

for i in range(n):
  s = []
  for j in range(n):
    s.append(room[j][i])

  room_x = ''.join(room[i]).split('X')
  room_y = ''.join(s).split('X')

  for j in range(len(room_x)):
    if len(room_x[j]) >= 2:
      answer_x += 1

  for j in range(len(room_y)):
    if len(room_y[j]) >= 2:
      answer_y += 1

print(answer_x, answer_y)