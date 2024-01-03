"""
1. 결과를 입력받을 빈 리스트, 방문 여부를 확인하는 bool 리스트 만들기

2. 만약 num이 m과 같다면 result 출력
   m개까지 result에 값을 담고 출력해야하기 때문

3. 1부터 n+1까지 for문을 돌면서
   만약 check[i]를 방문안했다면 check[i]를 True 변경
   result에 i 추가
   recur(num+1) <= 재귀함수
   
4. check[i] = False, result.pop()을 해주는 이유
   중간에 재귀함수로 불러서 이전의 for문이 계속 돌아가고 있기때문에
   이전값을 빼줘야 함
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
check = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num+1)
            check[i] = False
            result.pop()
    
recur(0)