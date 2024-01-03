## 맨헤튼 거리가 2인 걸 모든 경우의 수를 확인하려면 너무 조건이 복잡해짐
## 처음에 코드를 짤때 모든 경우의 수를 구하려고 하니 너무 지저분했음
## 현재 위치가 P이면 주변에 P가 1개 이상이면 거리두기를 실패한 것이고
## O이면 주변에 P가 2개 이상이면 거리두기를 실패한 것이다.

def solution(places):
    answer = [1] * len(places)
    
    for place in range(len(places)):
        tmp = places[place]
        for i in range(5):
            for j in range(5):
                cnt = 0
                if tmp[i][j] != 'X':
                    if i - 1 > -1:
                        if tmp[i-1][j] == 'P':
                            cnt += 1
                    if i + 1 < 5:
                        if tmp[i+1][j] == 'P':
                            cnt += 1
                    if j - 1 > -1:
                        if tmp[i][j-1] == 'P':
                            cnt += 1
                    if j + 1 < 5:
                        if tmp[i][j+1] == 'P':
                            cnt += 1
                            
                    if tmp[i][j] == 'P':
                        if cnt >= 1:
                            answer[place] = 0
                    elif tmp[i][j] == 'O':
                        if cnt >= 2:
                            answer[place] = 0
                    
    return answer