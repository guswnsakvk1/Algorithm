import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

mult = 0
plus = 0

for num in lst:
  tmp = 0
  while num != 0:
    if num % 2 == 0:
      tmp += 1
      num //= 2
    else:
      plus += 1
      num -= 1

  mult = max(mult, tmp)

print(mult + plus)