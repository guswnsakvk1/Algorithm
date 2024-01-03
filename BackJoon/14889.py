"""
1. 1~n 까지 n//2를 선택해서 만들 수 있는 모든 경우의 수 만들기
2. 모든 경우의 수의 합을 저장한 result 배열 만들기
3. result[i] + result[-1-i] 합이 answer보다 작으면 answer 업데이트
"""

import sys
input = sys.stdin.readline

def recur(num, s, lst):
    if num == n // 2:
        sum_num = 0

        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                sum_num += graph[lst[i]-1][lst[j]-1]
                sum_num += graph[lst[j]-1][lst[i]-1]
        
        result.append(sum_num)

        return
    
    for i in range(s, n+1):
        recur(num+1, i+1, lst+[i])

n = int(input())
graph = []
result = []
answer = 1e9

for _ in range(n):
    graph.append(list(map(int, input().split())))

recur(0, 1, [])

for i in range(len(result) // 2 + 1):
    answer = min(answer, abs(result[i] - result[-1 -i]))

print(answer)