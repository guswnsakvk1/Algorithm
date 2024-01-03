"""
lst의 i번째와 i-1의 차이를 사용해서 풀기
"""

n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

cnt = l
answer = 1

for i in range(1, n):
    num = lst[i] - lst[i-1]
    if num >= cnt:
        cnt = l
        answer += 1
    else:
        cnt -= num

print(answer)