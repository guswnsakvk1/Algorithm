## 색칠됬는지 확인하는 리스트를 만들어
## for문을 통해 붓 길이만큼씩 True로 바꾸기

def solution(n, m, section):
    answer = 0
    wall = [True] * n
    for i in section:
        wall[i-1] = False
        
    for i in range(n):
        if not wall[i]:
            answer += 1
            if i + m + 1 > n:
                num = n
            else:
                num = i + m
            for j in range(i, num):
                if not wall[j]:
                    wall[j] = True
    
    return answer