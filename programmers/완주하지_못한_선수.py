def solution(participant, completion):  
  # 정렬사용

  # participant.sort()
  # completion.sort()

  # for i in range(len(completion)):
  #     if participant[i] != completion[i]:
  #         return participant[i]

  # return participant[len(participant) -1]

  # 해쉬사용
  
  hashDict = {}
  sumHash = 0

  for part in participant:
      hashDict[hash(part)] = part
      sumHash += hash(part)

  for comp in completion:
      sumHash -= hash(comp)

  return hashDict[sumHash]