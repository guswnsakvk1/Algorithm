from itertools import combinations
import sys

input = sys.stdin.readline

L, K, C = map(int, input().split())
points = list(set(map(int, input().split())))
points.sort()
point_cnt = min(K, C, len(points))

if K == 1:
  answer = [points[0], max(L - points[0], points[0])]
else:
  cases = combinations(points, point_cnt)

  answer = [L, L]

  for case in cases:
    tmp = case[0]
    tree_len = 0
    for i in range(point_cnt-1):
      num = case[i+1] - case[i]
      if num > tree_len:
        tree_len = num

    tree_len = max(tree_len, L - case[-1])

    if answer[1] > tree_len:
      answer[0] = tmp
      answer[1] = tree_len
    elif answer[1] == tree_len:
      answer[0] = min(answer[0], tmp)

print(*answer)