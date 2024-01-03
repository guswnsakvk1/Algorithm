s = list(input())
t = list(input())

place = True

while len(s) != len(t):
  if place:
    if t[-1] == 'A':
      t.pop()
    else:
      t.pop()
      place = False
  else:
    if t[0] == 'A':
      t.pop(0)
    else:
      t.pop(0)
      place = True  

if not place:
  t = t[::-1]
  
if s == t:
  print(1)
else:
  print(0)