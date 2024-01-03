"""
1. board의 요소를 list형태로 변환하기
-> str은 str[0] = 'a'이런식으로 변환이 안되기 때문에 list형태로 변경

2. board에서 2x2로 붙어있는 블럭 위치를 tmp에 저장하기

3. tmp에 저장한 위치로 2x2 블럭위치를 공백으로 변경
※ 만약 tmp가 비어있다면 없어지는 블럭이 없기에 break

4. tmp안에 있는 모든 요소 삭제

5. board에 공백부분을 채우기
1) for문을 거꾸로해서 돌려서 밑에부터 공백을 채워나갈 거임 
2) 현재 위치가 공백일 경우
3) 1칸식 위로 가서 공백이 아닌 곳을 찾으면 그 값을 현재 위치에 저장

6. 공백의 개수를 return 하기
"""

def solution(m, n, board):
    answer = 0
    tmp = []
    
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ':
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        tmp.append((i, j))
                    
        if not tmp:
            break
    
        for i, j in tmp:
            board[i][j] = ' '
            board[i][j+1] = ' '
            board[i+1][j] = ' '
            board[i+1][j+1] = ' '
            
        tmp.clear()
    
        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == ' ':
                    num = i - 1
                    while num >= 0:
                        if board[num][j] != ' ':
                            board[i][j] = board[num][j]
                            board[num][j] = ' '
                            break
                        num -= 1
    
    for i in board:
        answer += i.count(' ')
    
    return answer