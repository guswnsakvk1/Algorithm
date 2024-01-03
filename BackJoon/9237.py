import sys
input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))
tree.sort(reverse=True)

answer = 0
for idx, day in enumerate(tree):
  answer = max(answer, idx+day+1)

print(answer+1)