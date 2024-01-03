"""
i번째가 i-1보다 작거나 같은 경우
i가 1이 아니면 i-1번째 값을 i번째 값에서 1뺀 값으로 변경
"""

import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  lst.append(int(input()))

answer = 0

for i in range(n-1, 0, -1):
  if lst[i] <= lst[i-1]:
    if lst[i] == 1:
      answer += lst[i-1] - 1
      lst[i+1] = 1
    else:
      answer += lst[i-1] - lst[i] + 1
      lst[i-1] = lst[i] - 1

print(answer)