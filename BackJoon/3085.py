"""
1. 인접한 요소의 위치를 바꾼다
2. 바꾼 배열을 통해 행, 열에서 가장 많이 사탕을 먹을 수 있는 지 확인한다.
3. 바꾼 요소를 다시 원위치 한다.
4. 모든 경우의 수까지 이 작업을 반복한다.

느낀점
1. 모든 경우의 수를 구할 때 배열을 추가로 만들어야 하는 지 안 만들어야 하는 지 생각해봐야한다고 느낌
2. 처음 시도할 때 copy로 새로운 계속 배열을 만드니깐 시간초과뜸
"""

import sys

def getAnswer(arr, n, answer):
    for i in range(n):
      num = 1
      for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
          num += 1
        else:
          num =1

        if num > answer:
          answer = num

      num= 1
      for j in range(1, n):
        if arr[j][i] == arr[j-1][i]:
          num += 1
        else:
          num = 1

        if num > answer:
          answer = num
                
    return answer

input = sys.stdin.readline
n = int(input())

bomboni = []
answer = 0

for i in range(n):
    bomboni.append(list(input()))

for i in range(n):
    for j in range(n-1):
        a = bomboni[i][j]
        b = bomboni[i][j+1]

        bomboni[i][j] = b
        bomboni[i][j+1] = a

        answer = getAnswer(bomboni, n, answer)

        bomboni[i][j] = a
        bomboni[i][j+1] = b

        c = bomboni[j][i]
        d = bomboni[j+1][i]

        bomboni[j][i] = d
        bomboni[j+1][i] = c

        answer = getAnswer(bomboni, n, answer)

        bomboni[j][i] = c
        bomboni[j+1][i] = d

print(answer)