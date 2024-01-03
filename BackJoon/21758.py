import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 오른쪽 방향으로 누적합
sum_lst1 = lst[:]
# 왼쪽 방향으로 누적합
sum_lst2 = lst[:]
for i in range(1, n):
  sum_lst1[i] = sum_lst1[i] + sum_lst1[i-1]
  sum_lst2[n-1-i] = sum_lst2[n-1-i] + sum_lst2[n-i]

left = 0
right = 0
mid = 0
for i in range(1, n-1):
  # 꿀 통이 왼쪽에 있을 경우 하나는 맨 오른쪽에 무조건 있어야 함
  # 나머지 하나는 하나씩 옮기면서 가장 큰 값 구하기
  left = max(left, sum_lst2[0]*2 - lst[-1] - sum_lst2[i] - lst[i])
  # 꿀 통이 오른쪽에 있을 경우 하나는 맨 왼쪽에 무조건 있어야 함
  # 나머지 하나는 하나씩 옮기면서 가장 큰 값 구하기
  right = max(right, sum_lst1[-1]*2 - lst[0] - sum_lst1[i] - lst[i])
  # 꿀 통이 가운데 있을 경우 맨 시작 시점은 오른쪽, 맨 왼쪽에 있어야 함
  # 가운데 꿀 통을 옮기면서 가장 큰 값 구하기
  mid = max(mid, sum_lst1[i] - sum_lst1[0] + sum_lst2[i] - sum_lst2[-1])

# 꿀통이 왼쪽, 오른쪽, 가운데 있을 경우의 수 가장 큰 값 출력
print(max(left, right, mid))