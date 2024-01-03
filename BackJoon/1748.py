"""
1. n자리 숫자이면 n-1 자리 숫자의 모든 경우의 수를 더해주기

2. n자리 숫자에서 10 ** (len(n) - 1) + 1 를 뺸 값에 len(n) 곱해주기
"""

n = input()

answer = 0
len_n = len(n)
for i in range(len(n)-1):
  answer += 9 * (10 ** i) * (i + 1)

answer += (int(n) - 10 ** (len_n - 1) + 1) * len_n
print(answer)