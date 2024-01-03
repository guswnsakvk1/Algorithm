import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 1e9

man = list(map(int, input().split()))
man.sort()

woman = list(map(int, input().split()))
woman.sort()

if n > m:
  for i in range(n-m+1):
    tmp = 0
    for j in range(m):
      tmp += abs(woman[j] - man[i+j])

    answer = min(answer, tmp)
elif n < m:
  for i in range(n-m+1):
    tmp = 0
    for j in range(n):
      tmp += abs(man[j] - man[i+j])

    answer = min(answer, tmp)
else:
  tmp = 0
  for i in range(n):
    tmp += abs(man[i] - woman[i])

  answer = tmp

print(answer)