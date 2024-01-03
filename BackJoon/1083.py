import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
s = int(input())

for i in range(N):
    if s == 0:
        break
    
    cnt = N - i

    if cnt <= s:
        num = max(lst[i:])
    else:
        num = max(lst[i:i+s+1])

    if lst[i] == num:
        continue
    else:
        idx = lst.index(num)

        for j in range(idx, i, -1):
            lst[j], lst[j-1] = lst[j-1], lst[j]
            s -= 1

print(*lst)