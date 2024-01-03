A, P = map(int, input().split())

lst = [A]
idx = 0

while True:
    num = 0

    while A != 0:
        A, b = divmod(A, 10)
        num += b ** P

    if num not in lst:
        lst.append(num)
        A = num
    else:
        idx = lst.index(num)
        break

print(idx)