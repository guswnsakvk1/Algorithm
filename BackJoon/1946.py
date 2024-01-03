import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  answer = n
  score = [0 for _ in range(n+1)]

  for i in range(n):
    a, b = map(int, input().split())
    score[a] = b

  minNum = score[1]
  for i in range(2, n+1):
    if(minNum < score[i]):
      answer -= 1
    else:
      minNum = score[i]

  print(answer)