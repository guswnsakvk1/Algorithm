"""
v1 : 행에 퀸이 있는지 저장하는 배열
v2 : 오른쪽 대각선에 퀸이 있는지 저장하는 배열
v3 : 왼쪽 대각선에 퀸이 있는지 저장하는 배열
"""

import sys

input = sys.stdin.readline

def recur(num, v1, v2, v3):
  global answer
  if num == n:
    answer += 1    
    return

  for i in range(n):
    if v1[i] == v2[num+i] == v3[num-i] == 0:
      v1[i] = v2[num+i] = v3[num-i] = 1
      recur(num+1, v1, v2, v3)
      v1[i] = v2[num+i] = v3[num-i] = 0
          
n = int(input())
answer = 0

v1 = [0] * n
v2 = [0] * (n * 2)
v3 = [0] * (n * 2)

recur(0, v1, v2, v3)
print(answer)