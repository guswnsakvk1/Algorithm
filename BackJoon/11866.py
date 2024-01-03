from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
answer = []

while len(answer) != n:
  for i in range(k-1):
    d.append(d.popleft())
  answer.append(d.popleft())

print("<", end="")
print(", ".join(map(str,answer)), end="")
print(">")