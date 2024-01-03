import heapq

n = int(input())
cardList = list(int(input()) for i in range(n))
heapq.heapify(cardList)
answer = 0

while len(cardList) != 1:
  num1 = heapq.heappop(cardList)
  num2 = heapq.heappop(cardList)
  sumNum = num1 + num2
  answer += sumNum
  heapq.heappush(cardList, sumNum)

print(answer)