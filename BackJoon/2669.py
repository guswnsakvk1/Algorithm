"""
1. x, y 최대가 100이니깐 행, 렬이 101인 0으로 초기화된 이중배열 만들기
2. 직사각형이 있는 위치에 1로 채우기
3. 이중배열 1인 개수 채우기
"""

answer = 0
graph = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      graph[i][j] = 1

for i in graph:
  answer += i.count(1)

print(answer)