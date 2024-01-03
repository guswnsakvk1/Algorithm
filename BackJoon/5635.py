"""
년, 월, 일 우선순위로 정렬한다
"""

import sys
input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
  lst.append(tuple(input().split()))

lst.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])))

print(lst[-1][0])
print(lst[0][0])