def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
        if len(basket) > 1:
            if basket[-2] == basket[-1]:
                basket.pop()
                basket.pop()
                answer += 2
                
    return answer