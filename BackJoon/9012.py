import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  vps = input()
  answer = 0
  for i in range(len(vps)):
    if answer < 0:
      break
    if(vps[i] == '('):
      answer += 1
    elif(vps[i] == ')'):
      answer -= 1

  if(answer == 0):
    print('YES')
  else:
    print('NO')