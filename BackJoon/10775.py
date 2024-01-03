import sys
input = sys.stdin.readline

def find(x):
  if x == parents[x]:
    return x
  parents[x] = find(parents[x])
  return parents[x]

n = int(input())
k = int(input())
answer = 0
parents = {i:i for i in range(n+1)}

airplane_lst = []
for _ in range(k):
  airplane_lst.append(int(input()))

for airplane in airplane_lst:
  x = find(airplane)

  if x == 0:
    break

  parents[x] = parents[x-1]
  answer += 1

print(answer)