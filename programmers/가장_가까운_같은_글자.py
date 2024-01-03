def solution(s):
    answer = [-1] * len(s)
    for i in range(1, len(s)):
        num = 0
        for j in range(i-1, -1, -1):
            num += 1
            if(s[i] == s[j]):
                answer[i] = num
                break
    
    return answer