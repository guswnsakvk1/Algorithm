import sys
input = sys.stdin.readline

index = 1

def check_A(index):
  if board_len - index >= 4:
    for i in range(index, index+4):
      if board[i] == '.':
        return False
    return True
  else:
    return False

def check_B(index):
  if board_len - index >= 2:
    for i in range(index, index+2):
      if board[i] == '.':
        return False
    return True
  else:
    return False

board = list(input().rstrip())

index = 0
board_len = len(board)

while index <= board_len-1:
  if board[index] == '.':
    index += 1
    continue

  change_A = check_A(index)
  change_B = check_B(index)

  if change_A:
    for i in range(index, index+4):
      board[i] = 'A'
    index += 4
    continue

  if change_B:
    for i in range(index, index+2):
      board[i] = 'B'
    index += 2
    continue

  print(-1)
  exit()

print(''.join(board))