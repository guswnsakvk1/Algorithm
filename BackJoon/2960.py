"""
1. 2부터 n까지 담긴 배열을 만든다.

2. int(math.sqrt(n)) + 1 까지 for문을 돌린다
※ sqrt를 쓰는 이유: 1 * 2 와 2 * 1은 같은 값이기 때문에

3. num * j가 n보다 작을 때까지 and num * j가 answer에 없을 경우
1) answer에 num * j 넣기
2) lst에서 num * j 없어개

4. 만약 lst가 비었을 경우 for문 멈추기
※ 반례 n = 2, k = 1 답 : 2
"""

import math

n, k = map(int, input().split())

answer = []

lst = [i for i in range(2, n+1)]

for i in range(int(math.sqrt(n)) + 1):
    j = 2
    num = lst.pop(0)
    answer.append(num)

    while num * j <= n:
        if num * j not in answer:
            answer.append(num * j)
            lst.remove(num * j)
        j += 1

    if not lst:
        break

print(answer[k-1])