import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_1 = []

for i in range(n):
    set_1.append(list(map(int, input().split())))

m, k = map(int, input().split())
set_2 = []

for i in range(m): 
    set_2.append(list(map(int, input().split())))

answer = [[0 for j in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            answer[i][j] += set_1[i][l] * set_2[l][j]

for i in answer:
    print(" ".join(map(str, i)))