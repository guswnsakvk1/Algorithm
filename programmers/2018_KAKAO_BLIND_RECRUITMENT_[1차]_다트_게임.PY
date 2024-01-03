def solution(dartResult):
    num = []
    check = False
    for i in range(len(dartResult)):
        if(dartResult[i] == 'S'):
            num[-1] **= 1
        elif(dartResult[i] == 'D'):
            num[-1] **= 2
        elif(dartResult[i] == 'T'):
            num[-1] **= 3
        elif(dartResult[i] == '*'):
            if(len(num) >= 2):
                num[-1] *= 2
                num[-2] *= 2
            else:
                num[-1] *= 2
        elif(dartResult[i] == '#'):
            num[-1] *= -1
        else:
            if(check):
                check = False
                continue
            if(dartResult[i+1] == '0'):
                num.append(10)
                check = True
            else:
                num.append(int(dartResult[i]))
                
    return sum(num)