## G = (현재 몸무게 ** 2) - (과거 몸무게 ** 2) 이므로
## sqrt(G + (과거 몸무게 ** 2)) = 현재 몸무게

import math

G = int(input())
answer = []

for i in range(1, 100000):
  num = G + i ** 2

  ## 양의 정수로 딱 떨어져야하기에 num을 int로 바꿔서
  ## 딱 떨어지는 지 확인
  if int(math.sqrt(num)) == math.sqrt(num):
    answer.append(int(math.sqrt(num)))

if answer:
  for i in answer:
    print(i)
else:
  print(-1)