def solution(rows, columns, queries):
    answer = []
    table = [[]]
    num = 1
    
    for i in range(rows):
        table.append([])
        for j in range(columns):
            table[i+1].append(num)
            num += 1
    
    for querie in queries:
        turn = 0
        minNum = 1e9
        row = querie[0]
        colum = querie[1]
        num = table[row][colum-1]
        while(True):
            if turn == 0 and colum != querie[3]:
                colum += 1
                if colum == querie[3]:
                    turn += 1
            elif turn == 1 and row != querie[2]:
                row += 1
                if row == querie[2]:
                    turn += 1
            elif turn == 2 and colum != querie[1]:
                colum -= 1
                if colum == querie[1]:
                    turn += 1
            elif turn == 3 and row != querie[0]:
                row -= 1
                
            save = table[row][colum-1]
            minNum = min(minNum, save)
            table[row][colum-1] = num
            num = save
            
            if row == querie[0] and colum == querie[1] and turn == 3:
                answer.append(minNum)
                break
            
    return answer