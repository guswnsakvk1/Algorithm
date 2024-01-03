n = int(input())
s = []
answers = []
cnt = 1
check = True

for i in range(n):
  num = int(input())
  while cnt <= num:
    s.append(cnt)
    answers.append('+')
    cnt += 1
  if(s[-1] == num):
    answers.append('-')
    s.pop()
  else:
    check = False

if(check):
  for answer in answers:
    print(answer)
else:
  print('NO')