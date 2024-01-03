import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
jewel = []

for _ in range(n):
  gram, price = map(int, input().split())
  # jewel에 gram은 최소힙으로 price는 최대힙으로 만들기
  heapq.heappush(jewel, (gram, -price))

h = []
for _ in range(k):
  heapq.heappush(h, int(input()))

prices = []
for _ in range(k):
  bag = heapq.heappop(h)

  # jewel이 있고 bag가 jewel에서 가장 작은 보석의 무게보다 클 경우
  while jewel and bag >= jewel[0][0]:
    # prices에 jewel에서 무게는 가장 작은 보석의 가격을 저장
    heapq.heappush(prices, heapq.heappop(jewel)[1])
  # 만약 prices가 있다면
  if prices:
    # answer에 가장 큰 값 더하기
    answer -= heapq.heappop(prices)
  # 만약 jewel이 없다면 
  elif not jewel:
    # 멈춤
    break

print(answer)