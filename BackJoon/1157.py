word = input()
lst = [0 for i in range(26)]

for i in word:
  if ('a' <= i <= 'z'):
    lst[ord(i)-97] += 1
  else:
    lst[ord(i)-65] += 1

answers = list(filter(lambda x: lst[x] == max(lst), range(len(lst))))
if(len(answers) > 1):
  print("?")
else:
  answer = int(answers[0]) + 65
  print(chr(answer))