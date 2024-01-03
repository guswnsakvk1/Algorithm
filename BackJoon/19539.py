import sys
input = sys.stdin.readline

n = int(input())

tree = list(map(int, input().split()))

num = sum(tree)
two = 0
one = 0

if num % 3 != 0:
  print('NO')
else:
  for t in tree:
    a, b = divmod(t, 2)
    two += a
    one += b

  if one > two:
    print('NO')
  elif (two - one) % 3 == 0:
    print('YES')