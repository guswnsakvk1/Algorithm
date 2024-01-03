n = int(input())

switch = list(map(int, input().split()))

k = int(input())

for i in range(k):
  sex, num = map(int, input().split())

  if sex == 1:
    for j in range(num-1, n, num):
      if switch[j]:
        switch[j] = 0
      else:
        switch[j] = 1
  else:
    if switch[num-1]:
      switch[num-1] = 0
    else:
      switch[num-1] = 1

    for l in range(n//2):
      if num + l > n or num - l < 1:
        break

      if switch[num - 1 - l] == switch[num - 1 + l]:
        if switch[num - 1 - l]:
          switch[num - 1 - l] = 0
        else:
          switch[num - 1 - l] = 1

        if switch[num - 1 + l]:
          switch[num - 1 + l] = 0
        else:
          switch[num - 1 + l] = 1
      else:
        break

for i in range(1, n+1):
    print(switch[i-1], end = " ")
    if i % 20 == 0 :
        print()