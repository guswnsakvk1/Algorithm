"""
순서대로 값을 확인하고 뒤집는 이유
1. 문제의 목적은 행렬 A를 행렬 B로 바꾸는 것
   따라서 행렬 A가 0인데 행렬 B에서 1이면 반드시 뒤집어야 함
2. 뒤집는 연산을 2번 이상 뒤집는 건 의미가 없음
3. 이때 최적의 선택은 반드시 뒤집어야 하는 칸을 뒤집고, 뒤집는 횟수를 최소화 하는것
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst1 = [list(input().rstrip()) for _ in range(n)]
lst2 = [list(input().rstrip()) for _ in range(n)]

answer = 0

def check_lst():
    for i in range(n):
        for j in range(m):
            if lst1[i][j] != lst2[i][j]:
                return False
    
    return True

def reverse_lst(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if lst1[i][j] == '0':
                lst1[i][j] = '1'
            else:
                lst1[i][j] = '0'

for i in range(n-2):
    for j in range(m-2):
        if lst1[i][j] != lst2[i][j]:
            reverse_lst(i, j)
            answer += 1

if check_lst():
    print(answer)
else:
    print(-1)