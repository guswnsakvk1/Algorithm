import itertools

def solution(k, dungeons):
  dungeons_count = len(dungeons)
  for i in range(dungeons_count, 0, -1):
    for cases in itertools.permutations(dungeons, i):
      now_k = k
      check = True
      for case in cases:
        if now_k >= case[0]:
          now_k -= case[1]
        else:
          check = False
          break
      if check:
          return i