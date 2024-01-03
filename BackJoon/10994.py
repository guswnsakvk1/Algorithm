## 사각형이 계속해서 만들어지는 규칙이 있음
## n이 1이 아닐때 n - 1 개의 사각형이 생김
## (0,0)에 사각형이 생긴후 (2,2)에 사각형이 생기고 (4,4)에 사각형이 생기고...
## 사각형 변의 길이는 4 * (n - 1) + 1
## 4 일때 13, 3 일때 9, 2 일때 5
N = int(input())
length = 4 * (N - 1) + 1
stars = [[' ' for i in range(length)] for j in range(length)]

def getAnswer(n, x, y):
  if n == 1:
    stars[y][x] = '*'
    return

  length = 4 * (n - 1) + 1
  
  for i in range(length):
    stars[y][x+i] = '*'
    stars[y+i][x] = '*'
    stars[y+length-1][x+i] = '*'
    stars[y+i][x+length-1] = '*'

  getAnswer(n-1, x+2, y+2)

getAnswer(N, 0, 0)

for star in stars:
  print("".join(star))