phone = input()
time = 0

for num in phone:
  if('A' <= num <= 'C'):
    time += 3
  elif('D' <= num <= 'F'):
    time += 4
  elif('G' <= num <= 'I'):
    time += 5
  elif('J' <= num <= 'L'):
    time += 6
  elif('M' <= num <= 'O'):
    time += 7
  elif('P' <= num <= 'S'):
    time += 8
  elif('T' <= num <= 'V'):
    time += 9
  else:
    time += 10

print(time)