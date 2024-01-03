n = input()
minuslst = []
pluslst = []
check = False
minNum = 0

for i in range(len(n)-1):
  if n[i] == '-':
    check = True
    pluslst = n[:i]
    minuslst = n[i+1:].replace('-', '+')
    break

if(check):
  minNum += sum(list(map(int,pluslst.split('+'))))
  minNum -= sum(list(map(int,minuslst.split('+'))))
else:
  minNum = sum(list(map(int,n.split('+'))))

print(minNum)