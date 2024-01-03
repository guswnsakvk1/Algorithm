n = int(input())
count = 0

def check():
  word = input()
  lst = [False for i in range(26)]
  prev = 0
  for i in range(len(word)):
    now = word[i]
    if(prev != now):
      if(lst[ord(now) - 97] == False):
        lst[ord(now) - 97] = True
        prev = now
      else:
        return False
  return True

for i in range(n):
  if(check() == True):
    count += 1

print(count)