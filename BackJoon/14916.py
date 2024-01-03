n = int(input())
five = n // 5

while five > -1:
  num = n - (5 * five)
  two = num // 2

  if five * 5 + 2 * two == n:
    print(five + two)
    break
  else:
    five -= 1

if five == -1:
  print(-1)