"""
https://aerocode.net/392 <- 풀이 참조
"""

import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
lst.sort()

answer = 1

for i in range(n):
  if answer < lst[i]:
    break

  answer += lst[i]

print(answer)