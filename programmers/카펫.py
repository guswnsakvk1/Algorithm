def solution(brown, yellow):
    divisor = []
    answer = []
    for i in range(yellow):
        if yellow % (i + 1) == 0:
            divisor.append(i+1)
            
    for i in range(len(divisor)):
        if (divisor[i] * 2) + (divisor[len(divisor) - (i + 1)] * 2) + 4 == brown:
            answer = [divisor[i] + 2, divisor[len(divisor) - (i + 1)] + 2]

    return answer