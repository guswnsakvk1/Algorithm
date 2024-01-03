n = int(input())
data = []
answer = [1 for _ in range(n)]

for i in range(n):
  data.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if(data[i][0] < data[j][0] and data[i][1] < data[j][1]):
      answer[i] += 1

print(" ".join(map(str, answer)))