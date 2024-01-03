"""
두 원의 내접 외접 공식을 사용해서 품
"""

import math
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  d = math.sqrt((x2- x1) ** 2 + (y2-y1) ** 2)

  
  if d == r1 == r2 == 0:
    print(1)
  elif d == 0 and r1 == r2:
    print(-1)
  elif abs(r1 - r2) < d < (r1 + r2): 
    print(2)
  elif r1 + r2 == d or abs(r1 - r2) == d:
    print(1)
  else:
    print(0)