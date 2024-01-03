"""
1. 가장 싼 패키지와 줄 낱개의 가격을 구한다.
2. 위에 구한 가격을 통해 만들 수 있는 모든 경우의 수 중 가장 작은 값을 구한다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 1e9
min_package = 1e9
min_one = 1e9

for _ in range(m):
    package, one = map(int, input().split())

    min_package = min(min_package, package)
    min_one = min(min_one, one)    

num = 0

while True:
    if (n - (num * 6)) < 0:
        one_cnt = 0
    else:
        one_cnt = (n - (num * 6))

    answer = min(answer, min_package * num + min_one * one_cnt)
    num += 1

    if n - (num * 6) < -6:
        print(answer)
        break