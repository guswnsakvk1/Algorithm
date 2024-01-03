n, m = map(int, input().split())

arr = []
dp = [[0 for _ in range(m+1)] for _ in range(n + 1)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input())

for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split())
    print(dp[end_x][end_y] - dp[end_x][start_y-1] - dp[start_x-1][end_y] + dp[start_x-1][start_y-1])