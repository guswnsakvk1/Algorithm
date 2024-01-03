"""
1. n이 0이면 빈배열로 deque 만들기
   n이 0이 아니면 arr[1:-1]를 deque 만들기

2. error가 나는지 확인하는 check 변수
   앞뒤 중 어디 요소 빼야하는 지 저장하는 pop_place 변수

3. p를 for문 돌리면서 
1) c가 R이면
   pop_place가 false면 True로
   True면 false로 바꾸기

2) c가 D이면
   pop_place가 false면 popleft()
   pop_place가 True면 pop

3) 만약 pop_place가 True면
   queue reverse하기
"""

import sys
from collections import deque

inpurt = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = input()
  n = int(input())
  arr = input()

  if n == 0:
    queue = deque([])
  else:
    queue = deque(arr[1:-1].split(','))

  check = False
  pop_place = False

  for c in p:
    if c == 'R':
      if pop_place:
        pop_place = False
      else:
        pop_place = True
    else:
      if n == 0:
        check = True
        break
      else:
        n -= 1
        if pop_place:
          queue.pop()
        else:
          queue.popleft()

  if pop_place:
    queue.reverse()

  if check:
    print('error')
  else:
    print('[' +  ",".join(queue) + ']')