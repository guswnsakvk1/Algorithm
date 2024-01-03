def solution(clothes):
    hashDict = {}
    for cloth in clothes:
        if cloth[1] in hashDict:
            hashDict[cloth[1]] += 1
        else:
            hashDict[cloth[1]] = 1

    answer = 1
    for cloth in hashDict:
        answer *= (hashDict[cloth] + 1)

    return answer - 1