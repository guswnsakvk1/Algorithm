"""
플로이드 알고리즘
1. 모든 노드 간 최단 경로를 구하는 알고리즘
2. 각 경로에서 새로운 중간 노드로 사용할 수 있는 노드를 선택하고
   더 짧은 길이를 선택하여 줄이는 과정을 반복
   ex) 1 -> 4 있다면 1 -> 2와 2 -> 4 둘을 합쳐서 더 짧은 길이를 선택
3. 초기값은 자기 자신을 제외한 모든 노드 값을 INF로 초기화
"""

INF = 40000000

def solution(n, s, a, b, fares):
    answer = INF
    
    dist = [[INF for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2]
        dist[edge[1]-1][edge[0]-1] = edge[2]
                
    floyd(dist, n)
    s -= 1
    a -= 1
    b -= 1
    
    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
    
    return answer

def floyd(dist, n):
    ## 중간 노드
    for i in range(n):
        ## 시작 노드
        for j in range(n):
            ## 끝 노드
            for k in range(n):
                if dist[j][i] + dist[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]