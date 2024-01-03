import sys
input = sys.stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

host = []
for _ in range(5):
    host.extend(map(int, input().split()))

for index, h in enumerate(host):
    check = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == h:
                bingo[i][j] = 0
                break

    for i in range(5):
        check_x = True
        check_y = True
        for j in range(5):
            if bingo[i][j] != 0:
                check_x = False
            if bingo[j][i] != 0:
                check_y = False

        if check_x:
            check += 1
        if check_y:
            check += 1
             
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4] == 0:
       check += 1

    if bingo[0][4] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[4][0] == 0:
       check += 1

    if check >= 3:
       print(index+1)
       break