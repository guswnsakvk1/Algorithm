def solution(lottos, win_nums):
  score = 1
  cnt_0 = lottos.count(0)
  for win_num in win_nums:
      if not(win_num in lottos) and score != 6:
          score += 1
  answer = [score - cnt_0 if (score - cnt_0 != 0) else 1, score]
  return answer