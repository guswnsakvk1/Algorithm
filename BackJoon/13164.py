import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

answer = []

for i in range(n-1):
  answer.append(lst[i+1] - lst[i])

answer.sort()

print(sum(answer[:n-k]))