n = int(input())

for i in range(n):
  lst = list(map(str, input().split()))
  for j in lst[1]:
    print(j * int(lst[0]), end='')
  print()