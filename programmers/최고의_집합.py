def solution(n, s):
    a, b = divmod(s, n)
    if a == 0:
        return [-1]
    else:
        answer = [a] * n
        idx = 0
        
        while b != 0:
            answer[idx] += 1
            b -= 1
            if idx == n-1:
                idx = 0
            else:
                idx += 1
        
        return answer[::-1]