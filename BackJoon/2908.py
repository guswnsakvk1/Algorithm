lst = list(map(str,input().split()))
for i in range(len(lst)):
  lst[i] = lst[i][::-1]

if(int(lst[0]) > int(lst[1])):
  print(lst[0])
else:
  print(lst[1])