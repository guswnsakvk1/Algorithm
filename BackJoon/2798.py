n, m = map(int, input().split())
cards = list(map(int,input().split()))
answer = cards[0]

for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      sumNum = cards[i] + cards[j] + cards[k]
      if(sumNum == m):
        answer = sumNum
      elif(sumNum > answer and sumNum < m):
        answer = sumNum

print(answer)