import copy
import sys
input = sys.stdin.readline

def dfs(cnt, board):
    if cnt == 5:
        max_num = 0
        for i in range(n):
            for j in range(n):
                if max_num < board[i][j]:
                    max_num = board[i][j]

        answer.append(max_num)
        return
    
    for i in range(4):
        if i == 0:
            dfs(cnt+1, moveRight(copy.deepcopy(board)))
        elif i == 1:
            dfs(cnt+1, moveLeft(copy.deepcopy(board)))
        elif i == 2:
            dfs(cnt+1, moveUp(copy.deepcopy(board)))
        else:
            dfs(cnt+1, moveDown(copy.deepcopy(board)))
            

def moveRight(board):
    for i in range(n):
        for j in range(n-1, -1, -1):
            num = j-1
            while num > -1:
                if board[i][num] == 0:
                    num -= 1
                    continue
                
                if board[i][j] == 0:
                    if board[i][num] != 0:
                        board[i][j] = board[i][num]
                        board[i][num] = 0
                        continue
                else:
                    if board[i][j] == board[i][num]:
                        board[i][j] += board[i][num]
                        board[i][num] = 0
                    break
                
    return board

def moveLeft(board):
    for i in range(n):
        for j in range(n):
            num = j+1
            while num < n:
                if board[i][num] == 0:
                    num += 1
                    continue
                
                if board[i][j] == 0:
                    if board[i][num] != 0:
                        board[i][j] = board[i][num]
                        board[i][num] = 0
                        continue
                else:
                    if board[i][j] == board[i][num]:
                        board[i][j] += board[i][num]
                        board[i][num] = 0
                    break
    
    return board

def moveUp(board):
    for i in range(n):
        for j in range(n):
            num = j+1
            while num < n:
                if board[num][i] == 0:
                    num += 1
                    continue
                
                if board[j][i] == 0:
                    if board[num][i] != 0:
                        board[j][i] = board[num][i]
                        board[num][i] = 0
                        continue
                else:
                    if board[j][i] == board[num][i]:
                        board[j][i] += board[num][i]
                        board[num][i] = 0
                    break
                    
    return board

def moveDown(board):
    for i in range(n):
        for j in range(n-1, -1, -1):
            num = j-1
            while num > -1:
                if board[num][i] == 0:
                    num -= 1
                    continue
                
                if board[j][i] == 0:
                    if board[num][i] != 0:
                        board[j][i] = board[num][i]
                        board[num][i] = 0
                        continue
                else:
                    if board[j][i] == board[num][i]:
                        board[j][i] += board[num][i]
                        board[num][i] = 0
                    break
    
    return board
            
n = int(input())
answer = []

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dfs(0, board)
print(max(answer))