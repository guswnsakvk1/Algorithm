"""
1. 각 마을에서 실을 수 있는 트럭용량을 배열로 저장
2. 빠른 도착지부터 출발지-도착지 사이의 택배용량을 줄여나가는 방법
"""

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

answer = 0
track = [C] * (N+1)
date = []

for _ in range(M):
  send, take, box = map(int, input().split())
  date.append((send, take, box))

date.sort(key=lambda x:(x[1], x[0]))

for send, take, box in date:
  min_weight = C
  
  for i in range(send, take):
    min_weight = min(min_weight, track[i])
  min_weight = min(min_weight, box)

  for i in range(send, take):
    track[i] -= min_weight

  answer += min_weight

print(answer)