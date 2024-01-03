import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 1, 7, 11, 71]
min_dp = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20, 28, 68, 88, 108, 188, 200]

for i in range(6, 101):
    max_dp.append(max_dp[i - 2] * 10 + 1)

num = '200'
n = 0
place = 2
tmp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
for i in range(18, 101):
    if '2' in num:
        if '0' in num:
            num = str(int(num) + (8 * (10 ** n)))
            min_dp.append(int(num))
            n += 1
        else:
            num = num.replace('2', '6')
            min_dp.append(int(num))
            n = tmp.pop(0)
    elif '6' in num:
        num = num.replace('6', '8')
        min_dp.append(int(num))
        num = '10' + '8' * place
        min_dp.append(int(num))
        place += 1
    elif '8' in num:
        if '0' in num:
            num = num.replace('0', '8')
            min_dp.append(int(num))
        else:
            num = '200' + '8' * (place-2)
            min_dp.append(int(num))

for _ in range(N):
    cnt = int(input())
    print(min_dp[cnt], max_dp[cnt])