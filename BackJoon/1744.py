n = int(input())
plusNum = []
minusNum = []
ones = []
answer = 0

for i in range(n):
  num = int(input())
  
  if num > 1:
    plusNum.append(num)
  elif num <= 0:
    minusNum.append(num)
  else:
    ones.append(num)

plusNum.sort(reverse=True)
minusNum.sort()

if(len(plusNum) % 2 == 0):
  for i in range(0, len(plusNum), 2):
    answer += plusNum[i] * plusNum[i+1]
else:
  for i in range(0, len(plusNum)-1, 2):
    answer += plusNum[i] * plusNum[i+1]
  answer += plusNum[len(plusNum)-1]

if(len(minusNum) % 2 == 0):
  for i in range(0, len(minusNum), 2):
    answer += minusNum[i] * minusNum[i+1]
else:
  for i in range(0, len(minusNum)-1, 2):
    answer += minusNum[i] * minusNum[i+1]
  answer += minusNum[len(minusNum)-1]

answer += len(ones)
print(answer)