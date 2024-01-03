import sys
input = sys.stdin.readline

N, L = map(int, input().split())

puddle = []
for _ in range(N):
    puddle.append(tuple(map(int, input().split())))

puddle.sort()
place = puddle[0][0]
answer = 0

for start, end in puddle:
    if place > end - 1:
        continue

    cnt, rest = divmod(end - max(start, place), L)
    num = cnt
    answer += cnt
    if rest:
        answer += 1
        num += 1
    
    if start > place:
        place = start
    place += num * L

print(answer)