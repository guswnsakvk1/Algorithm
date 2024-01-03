"""
1. 주어진 기호를 가지고 만들 수 있는 모든 경우의 수를 만들기
2. 기호의 배열에 따른 입력값을 순서대로 저장하기
3. 가장 큰 값과 가장 작은 값 출력

※ symbol에서 기호를 사용하면 개수 -1해주고 다시 +1해주어야 함
   +1 안해주면 되돌아올 때 제대로 작동하지 않음
"""

import sys

input = sys.stdin.readline

def recur(num, symbol,lst):
  if num == n - 1:
    result = num_lst[0]

    for i in range(n-1):
      if lst[i] == 'add':
        result += num_lst[i+1]
        
      if lst[i] == 'sub':
        result -= num_lst[i+1]
        
      if lst[i] == 'multiply':
        result *= num_lst[i+1]
        
      if lst[i] == 'division':
        if result < 0:
          result *= -1
          result //= num_lst[i+1]
          result *= -1
        else:
          result //= num_lst[i+1]

    answer.append(result)
        
    return

  if symbol['add'] > 0:
    symbol['add'] -= 1
    recur(num+1, symbol, lst + ['add'])
    symbol['add'] += 1

  if symbol['sub'] > 0:
    symbol['sub'] -= 1
    recur(num+1, symbol, lst + ['sub'])
    symbol['sub'] += 1

  if symbol['multiply'] > 0:
    symbol['multiply'] -= 1
    recur(num+1, symbol, lst + ['multiply'])
    symbol['multiply'] += 1

  if symbol['division'] > 0:
    symbol['division'] -= 1
    recur(num+1, symbol, lst + ['division'])
    symbol['division'] += 1

n = int(input())

answer = []
num_lst = list(map(int, input().split()))

add, sub, multiply, division = map(int, input().split())

recur(0, {'add' : add, 'sub' : sub, 'multiply' : multiply, 'division' : division }, [])

print(max(answer))
print(min(answer))