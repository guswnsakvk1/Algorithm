def solution(board):
    ## o의 개수를 저장하는 변수
    o_cnt = 0
    ## 빙고가 몇개인지 저장하는 변수
    o_win = 0
    ## o의 좌표를 저장하는 리스트
    o_coordinate = []
    
    ## x의 개수를 저장하는 변수
    x_cnt = 0
    ## 빙고가 몇개인지 저장하는 변수
    x_win = 0
    ## x의 좌표를 저장하는 리스트
    x_coordinate = []
    
    ## 빙고가 되는 모든 좌표를 저장한 리스트
    win_lst = [[(0,0),(0,1),(0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)], [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    
    for i in range(3):
        for j in range(3):
            ## 현재 좌표가 o이면
            if board[i][j] == 'O':
                ## o_cnt 1증가
                o_cnt += 1
                ## 현재 좌표 저장
                o_coordinate.append((i, j))
            ## 현재 좌표가 x이면
            elif board[i][j] == 'X':
                ## x_cnt 1증가
                x_cnt += 1
                ## 현재 좌표 저장
                x_coordinate.append((i, j))
    
    ## 빙고는 o,x 개수가 3이상일 때만 확인하면 됨

    if o_cnt >= 3:
        for win in win_lst:
            ## 빙고하는 좌표가 들어있는 지 확인하는 변수
            cnt = 0
            for coordinate in win:
                ## 빙고 좌표가 o_coordinate 있다면
                if coordinate in o_coordinate:
                    ## cnt 1증가
                    cnt += 1
            ## o는 선공이므로 1, 2빙고까지만 되므로
            ## 3 빙고가 되면 return 0
            if o_win == 3 and cnt == 3:
                return 0
            ## 아니면
            elif cnt == 3:
                ## o_win 1증가
                o_win += 1
                ## cnt 0으로 초기화
                cnt = 0
                    
    if x_cnt >= 3:
        for win in win_lst:
            ## 빙고하는 좌표가 들어있는 지 확인하는 변수
            cnt = 0
            for coordinate in win:
                ## 빙고 좌표가 o_coordinate 있다면
                if coordinate in x_coordinate:
                    ## cnt 1증가
                    cnt += 1
            ## x는 선공이므로 1, 2빙고까지만 되므로
            ## 3 빙고가 되면 return 0
            if x_win == 1 and cnt == 3:
                return 0
            ## 아니면
            elif cnt == 3:
                ## x_win 1증가
                x_win = 1
                ## cnt 0으로 초기화
                cnt = 0

    ## o이 1, 2개 빙고이고 x는 빙고가 아니고 o의 개수와 x의 개수가 차이가 1이면
    if (o_win == 1 or o_win == 2) and x_win == 0 and o_cnt - x_cnt == 1:
        return 1
    ## o이 빙고가 없고 x가 빙고가 1개이고 o의 개수와 x의 개수가 같으면
    elif o_win == 0 and x_win == 1 and o_cnt - x_cnt == 0:
        return 1
    ## o, x 둘다 빙고가 아니고 o의 개수와 x의 개수 차이가 1, 0이면
    elif (o_cnt - x_cnt == 1 or o_cnt - x_cnt == 0) and o_win == 0 and x_win == 0:
        return 1
    else:
        return 0