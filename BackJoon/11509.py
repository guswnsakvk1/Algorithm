import sys
input = sys.stdin.readline

n = int(input())
balloon = list(map(int, input().split()))
lst = [0] * 1000001

for b in balloon:
    if lst[b]:
        lst[b] -= 1

    lst[b-1] += 1 

print(sum(lst))