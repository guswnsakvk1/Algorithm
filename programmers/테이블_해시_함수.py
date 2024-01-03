def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin, row_end+1):
        num = 0
        for j in range(len(data[0])):
            num += (data[i-1][j] % i)
            
        answer ^= num
    
    return answer