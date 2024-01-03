import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
array = list(input())

for i in range(N):
    if array[i] == 'P':
        start = max(i - K, 0)
        end = min(i + K, N)

        for i in range(start, end+1):
            if array[i] == 'H':
                answer += 1
                array[i] = 0
                break

print(answer)