import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    k = int(input())
    lst = list(map(int, input().split()))

    result = 0
    max_num = lst[-1]

    for i in range(k-1, -1, -1):
        if lst[i] > max_num:
            max_num = lst[i]
        else:
            result += max_num - lst[i]

    print(result)