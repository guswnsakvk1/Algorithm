## 입력된 lst의 요소의 순서도 생각해야함
## 요소를 여러번 사용할 수 있으므로 중복순열사용
import itertools

n, k = input().split()
lst = list(map(str, input().split()))
length = len(n)

while True:
  answer = []
  arr = itertools.product(lst, repeat = length)

  for i in arr:
    num = "".join(i)
    if int(num) <= int(n):
      answer.append(num)

  if len(answer) >= 1:
    print(max(answer))
    break
  else:
    length -= 1