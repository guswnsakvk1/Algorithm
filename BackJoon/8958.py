n = int(input())
case = [ [] for i in range(n)]
for i in range(n):
  result = 0
  sum = 0
  case[i] = input()
  for j in range(len(case[i])):
    if case[i][j] == "O":
      sum += 1
      result += sum
    else:
      sum = 0
  print(result)