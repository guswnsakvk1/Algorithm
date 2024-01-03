import sys
input = sys.stdin.readline

global answer

def solve(x, y, size, color):
  global answer
  if size == 1:
    answer[color] += 1
    return

  check = False

  for i in range(x, x+size):
    for j in range(y, y+size):
      if colored_paper[i][j] != color:
        check = True
        
  num = size // 2
  if check:
    solve(x, y, num, colored_paper[x][y])
    solve(x, y + num, num, colored_paper[x][y + num])
    solve(x + num, y, num, colored_paper[x + num][y])
    solve(x + num, y + num, num, colored_paper[x + num][y + num])
  else:
    answer[color] += 1
  
N = int(input())
colored_paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

solve(0, 0, N, colored_paper[0][0])

print(answer[0])
print(answer[1])