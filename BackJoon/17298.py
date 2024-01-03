n = int(input())
lst = list(map(int,input().split()))
stack = []
result = [-1 for _ in range(n)]

for i in range(n):
    while stack and lst[stack[-1]] < lst[i]:
        result[stack.pop()] = lst[i]
    stack.append(i)
print(*result)