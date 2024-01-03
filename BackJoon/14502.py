"""
1. n x m 크기 graph에서 0의 위치와 2의 위치를 zero, two에 저장한다.

2. zero에 있는 값으로 만들 수 있는 모든 조합의 경우의 수를 리스트(comb)를 만든다.

3. graph를 복사하여 zero의 경우의 수에 따른 기둥을 설치한다.

4. graph를 복사한 이중배열에 dfs를 사용해서 0이 가장 많은 때를 구한다.
"""

from itertools import combinations
from collections import deque
import copy

def bfs(tmp_graph, virus, dx, dy, answer, n, m):
    queue = deque()
    for v in virus:
        queue.append(v)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 1
                queue.append((nx, ny))

    num = 0
    
    for i in tmp_graph:
        num += i.count(0)

    if num > answer:
        answer = num

    return answer

n, m = map(int, input().split())

graph = []
zero = []
virus = []
answer = 0

for i in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)
    for j in range(m):
        if lst[j] == 0:
            zero.append((i, j))

        if lst[j] == 2:
            virus.append((i, j))

comb = combinations(zero, 3)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for com in comb:
    tmp_graph = copy.deepcopy(graph)
    for c in com:
        tmp_graph[c[0]][c[1]] = 1

    answer = bfs(tmp_graph, virus, dx, dy, answer, n, m)

print(answer)