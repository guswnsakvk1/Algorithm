import copy

n = int(input())
coin = [list(input()) for _ in range(n)]
rev_coin = copy.deepcopy(coin)
answer = n * n

for i in range(n):
  for j in range(n):
    if rev_coin[i][j] == 'T':
      rev_coin[i][j] = 'H'
    else:
      rev_coin[i][j] = 'T'

for bit in range(2 ** n):
  tmp_coin = []
  for i in range(n):
    if bit & (1 << i):
      tmp_coin.append(rev_coin[i])
    else:
      tmp_coin.append(coin[i])

  cnt = 0
  for i in range(n):
    tmp_cnt = 0
    for j in range(n):
      if tmp_coin[j][i] == 'T':
        tmp_cnt += 1

    cnt += min(tmp_cnt, n-tmp_cnt)

  answer = min(answer, cnt)

print(answer)