ntopia = input()

ucpc = ['U', 'C', 'P', 'C']
num = 0

for s in ntopia:
  if s == ucpc[num]:
    num += 1

  if num == 4:
    break

if num == 4:
  print('I love UCPC')
else:
  print('I hate UCPC')