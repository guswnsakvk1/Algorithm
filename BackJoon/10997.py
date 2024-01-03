N = int(input())
## 재귀로 반복되는 변의 처음 시작 길이
length = 4 * (N - 1) + 1
stars = [[' ' for i in range(length)] for j in range(4 * N - 1)]
cnt = -1
## 별찍기 좌표
## x1, y1은 밑에 쪽에서 시작하는 좌표
x1, y1 = length - 1, 4 * N - 2
## x2, y2는 위쪽에서 시작하는 좌표
x2, y2 = 0, 0

def getAnswer(n, x1, y1, x2, y2, cnt):
  cnt += 1
  if n == 1:
    return
  
  ## cnt가 짝수, 홀수에 따라서 시작하는 좌표가 달라짐
  ## 짝수면 x1, y1으로 홀수면 x2, y2
  if cnt % 2 == 0:
    for i in range(n):
      stars[y1][x1-i] = '*'
      stars[y1-i][x1] = '*'
    getAnswer(n-2, x1, y1, x2 + 2, y2 + 2, cnt)
  else:
    for i in range(n):
      stars[y2][x2+i] = '*'
      stars[y2+i][x2] = '*'
    getAnswer(n-2, x1 - 2, y1 - 2, x2, y2, cnt)

if N == 1:
  print('*')
else:
  ## 제일 위 변과 제일 왼쪽의 변은 "*"로 채우고 시작
  stars[0] = ['*' for _ in range(length)]
  for i in range(len(stars)):
    stars[i][0] = "*"
  ## 두번째 리스트에는 무조건 "*"이 한개 있음
  stars[1] = ["*"]

  getAnswer(length, x1, y1, x2, y2, cnt)
  
  for i in stars:
    print("".join(i))