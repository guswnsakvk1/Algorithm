from collections import deque

n, m = map(int,input().split())

global answer
answer = -1

def bfs(num, cnt, want):
    global answer
    ## 현재 숫자와 몇 번째인지를 저장하는 queue
    queue = deque()
    queue.append((num, cnt))

    while queue:
        x, y = queue.popleft()
        ## 현재 숫자가 want와 같으면 멈춤
        if x == want:
            answer = y
            break
        ## 현재 숫자가 want보다 크면 무시하고 계속 진행
        elif x > want:
            continue
        
        queue.append((x*2, y+1))
        queue.append((x*10+1, y+1))

    ## answer가 -1이 아니면 answer에 +1해서 출력
    if answer != -1:
        return answer + 1
    ## 아니면 -1출력
    else:
        return -1
    
print(bfs(n, 0, m))