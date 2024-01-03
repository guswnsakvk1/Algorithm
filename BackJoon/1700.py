from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(map(int, input().split()))

answer = 0
socket = []

while queue:
    num = queue.popleft()

    # 코드에 이미 꽂혀져있음
    if num in socket:
        continue
    
    # 코드 자리 남음
    if len(socket) < n:
        socket.append(num)
        continue
    
    tmp = []
    check = False

    # 현재 코드에 연결된 전기 용품 중 앞으로 가장 늦게 사용되는 전기용품 찾기
    for i in range(n):
        pluged = socket[i]

        if pluged in queue:
            index = queue.index(pluged)
        else:
            index = 101
            check = True
        
        tmp.append(index)

        if check:
            break
    
    # 찾은 전기용품 코드에서 뽑기
    plug_out = tmp.index(max(tmp))
    del socket[plug_out]

    # 새로운 전기 용품 연결
    socket.append(num)
    answer += 1

print(answer)