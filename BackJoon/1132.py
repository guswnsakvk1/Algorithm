import sys
input = sys.stdin.readline

N = int(input())

answer = 0
first_alphabet = set()
alphabet = {
  'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,
  'H':0,'I':0, 'J':0}

for _ in range(N):
  lst = list(input().rstrip())
  lst.reverse()

  first_alphabet.add(lst[-1])

  for idx, num in enumerate(lst):
    alphabet[num] += 10 ** idx

alphabet = sorted(alphabet.items())
alphabet.sort(key=lambda x:x[1])

if alphabet[0][0] in first_alphabet:
    for j in range(1, 10):
      if alphabet[j][0] not in first_alphabet:
        alphabet.insert(0, alphabet[j])
        del alphabet[j+1]
        break

for i in range(10):
  answer += alphabet[i][1] * i

print(answer)