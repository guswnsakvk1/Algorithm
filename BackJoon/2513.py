import sys
input = sys.stdin.readline

N, K, S = map(int, input().split())

answer = 0
cnt = 0
left = []
right = []

for _ in range(N):
    place, people = map(int, input().split())
    if S > place:
        left.append([place, people])
    else:
        right.append([place, people])

left.append([S, 0])
right.append([S, 0])

left.sort()
right.sort(reverse=True)

print(left)
print(right)

for i in range(len(left)):
    cnt += left[i][1]

    if cnt >= K:
        num, rest = divmod(cnt, K)

        answer += (S  - left[i][0]) * num * 2
        cnt = rest
        if rest:
            answer += left[i+1][0] - left[i][0]
        else:
            answer -= left[i+1][0] - left[i][0]
    else:
        if i+1 != len(left):
            answer += left[i+1][0] - left[i][0]

cnt = 0

for i in range(len(right)):
    cnt += right[i][1]

    if cnt >= K:
        num, rest = divmod(cnt, K)

        answer += (right[i][0] - S) * num * 2
        cnt = rest

        if rest:
            answer += right[i][0] - right[i+1][0]
        else:
            answer -= right[i][0] - right[i+1][0]
    else:
        if i+1 != len(right):
            answer += right[i][0] - right[i+1][0]

if left:
    answer += left[0][0]

if right:
    answer += right[0][0]

print(answer)