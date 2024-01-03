import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  ADDH, ADDT, MINT, ADDO, MINO = 0,0,0,0,0

  ADDH += N // 60
  N %= 60
  ten, one = divmod(N, 10)
  
  if N <= 35:
    if one >= 6:
      ADDT = ten + 1
      MINO = 10 - one
    else:
      ADDT = ten
      ADDO = one
  else:
    ADDH += 1
    if one >= 5:
      MINO = 10 - one
      MINT = 5 - ten
    else:
      ADDO = one
      MINT = 6 - ten

  print(ADDH, ADDT, MINT, ADDO, MINO)