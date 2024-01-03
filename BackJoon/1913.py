n = int(input())
target = int(input())

start = (n -1) // 2
x, y = start, start
target_X, target_y = start, start

snail = [[0 for _ in range(n)] for _ in range(n)]
num = 0
count = 1

for i in range(n//2+1):
    num += 1
    snail[x][y] = num

    if num == target:
        target_X = x
        target_y = y

    if i == 0:
        x -= 1
        continue

    for j in range(count):
        y += 1
        num += 1
        snail[x][y] = num
        if num == target:
            target_X = x
            target_y = y

    for j in range(count+1):
        x += 1
        num += 1
        snail[x][y] = num
        if num == target:
            target_X = x
            target_y = y

    for j in range(count+1):
        y -= 1
        num += 1
        snail[x][y] = num
        if num == target:
            target_X = x
            target_y = y

    for j in range(count+1):
        x -= 1
        num += 1
        snail[x][y] = num
        if num == target:
            target_X = x
            target_y = y

    x -= 1
    count += 2

for s in snail:
    print(*s)

print(target_X+1, target_y+1)