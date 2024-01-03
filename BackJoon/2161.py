"""
1. 1은 무조건 처음에 나오므로 answer에 1넣기
2. queue는 2~n 까지 초기화
3. queue가 빌때까지
   queue에 값을 꺼내서 넣고
   answer에 queue값을 넣기
"""

from collections import deque

n = int(input())
answer = [1]
queue = deque([i for i in range(2, n+1)])

while queue:
    queue.append(queue.popleft())
    answer.append(queue.popleft())

print(" ".join(map(str, answer)))