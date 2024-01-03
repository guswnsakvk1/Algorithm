import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  answer = 0
  n = int(input())
  lst = list(map(int, input().split()))
  lst.sort()

  new_lst = []

  for i in range(0,n,2):
    new_lst.append(lst[i])

  if n % 2 == 0:
    for i in range(n-1, 0, -2):
      new_lst.append(lst[i])
  else:
    for i in range(n-2, 0, -2):
      new_lst.append(lst[i])

  for i in range(n-1):
    answer = max(answer , abs(new_lst[i+1] - new_lst[i]))
  
  print(max(answer, abs(new_lst[-1] - new_lst[0])))