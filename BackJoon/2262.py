import sys
input = sys.stdin.readline

n = int(input())
rank = list(map(int, input().split()))
answer = 0

for i in range(n-1):
  target = max(rank)
  idx = rank.index(target)

  if idx == 0:
    answer += target - rank[idx+1]
  elif idx == len(rank)-1:
    answer += target - rank[idx-1]
  else:
    answer += min(target - rank[idx+1], target - rank[idx-1])

  rank.remove(target)
print(answer)