import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0

while True:
  bottle = N + answer
  cnt = 0

  while bottle > 0:
    if bottle % 2 != 0:
      cnt += 1

    bottle //= 2

  if cnt <= K:
    break

  answer += 1

print(answer)