"""
1. lock의 배열에 상하좌우에 len(lock)-1 추가
2. key를 lock 배열에 한칸 식 이동하면서 한 위치에서 4번 회전
3. 모든 위치에서 key를 회전하는데 
1) lock이 모두 1이면 return True
2) 모든 경우에서 실패하면 return False

------

1. 58 x 58 array 만들기
1) lock의 최대 크기가 20 x 20이기 때문

2. array에 lock을 옮김
1) lock을 옮길 때 offset부터 offset + len(lock)까지
2) offset 부분부터 저장하는 이유 : key를 돌리면서 lock이 전부다 1로 되는 지 확인하기 위함

3. match 함수를 사용해서 key를 돌리면서 array에 key값 더하기
1) 키값을 더해서 모든 키값이 1이 되는 지 확인하기 위함

4. check 함수를 사용해서 lock이 모두 1이면 return True

5. 아니면 return False
"""

def solution(key, lock):
    offset = len(lock) - 1
    
    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for turn in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]
                
                match(r, c, turn, arr, key)
                
                if check(offset, arr, lock):
                    return True
                
    return False

def match(r, c, turn, arr, key):
    n = len(key)

    for i in range(n):
        for j in range(n):
            if turn == 0:
                arr[r+i][c+j] += key[i][j]
            elif turn == 1:
                arr[r+i][c+j] += key[j][n-1-i]
            elif turn == 2:
                arr[r+i][c+j] += key[n-1-i][n-1-j]
            else:
                arr[r+i][c+j] += key[n-1-j][i]

def check(offset, arr, lock):
    n = len(lock)
    
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
            
    return True