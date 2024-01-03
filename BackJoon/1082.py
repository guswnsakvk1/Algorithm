import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())

number = {}
for idx, num in enumerate(P):
  try:
    number[num] = max(number[num], idx)
  except:
    number[num] = idx

number = sorted(number.items())

dp = [0] * (M+1)

for i in range(1, M+1):
  num = 0
  for key, value in number:
    if i - key < 0:
      continue

    tmp = list(str(dp[i - key]))
    tmp.append(str(value))
    tmp.sort(reverse=True)
    num = max(num, int("".join(tmp)))

  dp[i] = num

print(max(dp) // 10)