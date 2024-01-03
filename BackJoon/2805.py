import sys
input = sys.stdin.readline

n, target = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
result = 0

while start <= end:
  mid = (start + end) // 2
  tree = 0

  for num in lst:
    if num > mid:
      tree += num - mid

  if tree < target:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)