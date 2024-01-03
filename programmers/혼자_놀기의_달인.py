def solution(cards):
    boxs = []
    visited = [False] * (len(cards) + 1)
    
    for i in range(len(cards)):
        if visited[i+1]:
            continue
            
        box = []
        
        while not visited[i+1]:
            box.append(cards[i])
            visited[i+1] = True
            i = cards[i]-1
        
        boxs.append(box)
        
    if len(boxs) == 1:
        return 0
    else:
        boxs.sort()
        return len(boxs[-1]) * len(boxs[-2])