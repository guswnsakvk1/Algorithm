"""
1. 숫자 num은 최소 lst[num]의 위치에서부터 있을 수 있음
2. answer[num]이 == 0 이거나 answer[:num]에 있는 0의 개수가
   num보다 크면 answer[num]에 num으로 업데이트
3. 아니면 뒤로 한칸씩 뒤로 옮겨서 조건확인
"""

n = int(input())
lst = list(map(int, input().split()))
answer = [0] * n
num = 1

for i in lst:
  for j in range(i, n):
    tmp = answer[:j]
    cnt = tmp.count(0)
    if answer[j] == 0 and cnt >= i:
      answer[j] = num
      num += 1
      break

print(*answer)