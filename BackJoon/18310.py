n = int(input())
lst = list(map(int, input().split()))
lst.sort()

num = n // 2
if n % 2 == 0:
    num -= 1

print(lst[num])