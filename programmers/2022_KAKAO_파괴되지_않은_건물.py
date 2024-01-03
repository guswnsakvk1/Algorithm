def solution(board, skill):
    answer = 0
    ## 누적합을 저장할 리스트
    pre = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    ## 누적합 초기화할 반복분
    for kind, start_x, start_y, end_x, end_y, power in skill:
        if kind == 1:
            power *= -1
        pre[start_x][start_y] += power
        pre[start_x][end_y + 1] += (power * -1)
        pre[end_x + 1][start_y] += (power * -1)
        pre[end_x + 1][end_y + 1] += power
    
    ## 가로로 누적합을 저장하는 반복문
    for i in range(len(pre)-1):
        for j in range(1, len(pre[0])-1):
            pre[i][j] += pre[i][j-1]
            
    ## 세로로 누적합을 저장하는 반복분
    for i in range(len(pre[0])-1):
        for j in range(1, len(pre)-1):
            pre[j][i] += pre[j-1][i]
    
    ## board와 pre의 요소를 더해서 0보다 크면 answer에 +1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + pre[i][j] > 0:
                answer += 1
                
    return answer