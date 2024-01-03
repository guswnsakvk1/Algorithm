## 조합

"""
1. 조합을 사용해서 모든 경우의 수를 구한다
2. 모든 경우의 수를 join으로 출력
"""

from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

comb = combinations(num, m)

for c in comb:
    print(' '.join(map(str, c)))


#### 멀티 트리 방법

def recur(num, s, lst):
  if num == m:
    answer.append(lst)
    return

  for i in range(s, n+1):
    recur(num+1, i+1, lst + [i])
    
n, m = map(int, input().split())

answer = []
recur(0, 1, [])

for a in answer:
  print(' '.join(map(str, a)))