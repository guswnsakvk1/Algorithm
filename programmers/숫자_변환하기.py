## deque를 사용해서 안에 값을 2로 나누거나, 3으로 나누거나, n을 뺀 값을 저장
## 모든 경우의 수를 다 진행해야하지게 가능한 모든 것을 진행
## 만약 x가 deque에 있으면 for문의 i+1을 return
## 아니면 -1을 return
import collections

def solution(x, y, n):
    answer = 0
    deq = collections.deque([y])
    
    ## x와 y가 갔다면 0을 리턴
    if x == y:
        return 0
    
    ## x에 n을 계속 더해서 y를 만드는 방법이 가장 많은 회수를 요구함
    ## 따라서 i 범위를 (y-x)//n 까지
    for i in range((y-x)//n):
        for j in range(len(deq)):
            num = deq.popleft()
            if num < x:
                continue
            
            if num % 2 == 0:
                deq.append(num // 2)
            if num % 3 == 0:
                deq.append(num // 3)
            if num - n >= x:
                deq.append(num - n)
        
        if x in deq:
            answer = i + 1
            break
        
    return answer if answer != 0 else -1