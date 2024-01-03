def solution(board):
    ## 첫 번째 리스트에 있는 값은 변환이 안되기에
    ## 첫 번째 리스트에 1이 있으면 최소값을 1로 설정
    answer = 1 if 1 in board[0] else 0

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            ## board[i][j]가 1이 아니면 정사각형이 안됨
            ## board[i][j]가 1일 경우에만 더 큰 정사각형이 되는지 확인
            if board[i][j] > 0:
                board[i][j] = min(board[i][j-1], board[i-1][j-1], board[i-1][j]) + 1
            ## board[i][j]가 answer보다 클경우
            ## 더 큰 정사각형이 되므로 answer값 변경
            if answer < board[i][j]:
                answer = board[i][j]
    
    return answer ** 2