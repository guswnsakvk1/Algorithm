n = int(input())
for i in range(n):
  scores = list(map(int, input().split()))
  student = scores[0]
  avg = (sum(scores) - student) / student
  p = 0
  for j in range(1, student+1):
    if avg < scores[j]:
      p += 1
  print("{:.3f}%".format(round(((100 / student) * p),3)))