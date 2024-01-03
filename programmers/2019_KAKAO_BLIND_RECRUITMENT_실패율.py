def solution(N, stages):
    answer = []
    player = len(stages)
    dictionary={}
    for i in range(N):
        cnt = stages.count(i+1)
        if player == 0:
            dictionary[i+1] = 0
        else:
            dictionary[i+1] = cnt / player
        player -= cnt
    answer = [stage[0] for stage in sorted(dictionary.items(), key=lambda x: x[1], reverse=True)]
    return answer