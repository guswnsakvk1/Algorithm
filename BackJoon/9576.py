import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  answer = 0

  number = [True] * (n+1)
  lst = []
  for i in range(m):
    a, b = map(int, input().split())
    lst.append((a, b))

  lst.sort(key=lambda x:(x[1], x[0]))

  for a,b in lst:
    for i in range(a, b+1):
      if number[i]:
        answer += 1
        number[i] = False
        break

  print(answer)