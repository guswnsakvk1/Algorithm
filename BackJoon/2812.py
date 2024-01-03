n, k = map(int, input().split())

lst = list(map(int, input()))

stack = []
max_num = lst[0]
count = k

for i in range(n):
  if count == 0:
    stack.append(lst[i])
    continue
  
  if not stack:
    stack.append(lst[i])
  else:
    if lst[i] > max_num:
      max_num = lst[i]

    while stack and count != 0 and stack[-1] < max_num:
      if stack[-1] < lst[i]:
        count -= 1
        stack.pop()
      else:
        break

    stack.append(lst[i])

print("".join(map(str, stack[:n-k])))