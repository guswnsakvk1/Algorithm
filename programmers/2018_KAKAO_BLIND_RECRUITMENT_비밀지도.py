def solution(n, arr1, arr2):
    answer = [] * n
    newArr1 = []
    newArr2 = []
    for num in arr1:
        newNum = bin(num)
        newArr1.append(newNum[2:].zfill(n))
    
    for num in arr2:
        newNum = bin(num)
        newArr2.append(newNum[2:].zfill(n))
        
    for i in range(n):
        result = ''
        for j in range(n):
            if newArr1[i][j] == '1':
                result += '#'
            elif newArr2[i][j] == '1':
                result += '#'
            else:
                result += ' '
            if(len(result) == n):
                answer.append(result)

    return answer