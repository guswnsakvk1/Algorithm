import sys

input = sys.stdin.readline

N = int(input())
a,b,c,d,e,f = map(int,input().split())

max_dice = max(a,b,c,d,e,f)
min_dice = min(a,b,c,d,e,f)

two = []
two.append(a+b)
two.append(a+c)
two.append(a+d)
two.append(a+e)
two.append(b+c)
two.append(b+d)
two.append(b+f)
two.append(c+e)
two.append(c+f)
two.append(d+e)
two.append(d+f)
two.append(e+f)
two.sort()

three = []
three.append(a+b+c)
three.append(a+b+d)
three.append(a+c+e)
three.append(a+d+e)
three.append(b+c+f)
three.append(b+d+f)
three.append(c+e+f)
three.append(d+e+f)
three.sort()

if N == 1:
  print(a + b + c + d + e + f - max_dice)
elif N == 2:
  print(three[0]*4 + two[0]*4)
else:
  print(three[0]*4 + (N-1)*two[0]*4 + (N-2)*two[0]*4 + (N-1) * (N-2) * min_dice*4 + (N-2)*(N-2)*min_dice)