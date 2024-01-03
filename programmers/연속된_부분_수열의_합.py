"""
누적 합 행렬을 사용해서 구간합을 계산해서 답을 추출한다.
수열이 오름차순으로 정렬되어 있기에 위치를 저장하는 변수를 2개 만들어
k와 값이 같아지는 부분을 찾는다.

pre라는 변수는 그대로 두고 now라는 변수를 뒤로 이동시키면서 k값에 근접하게 만든다.
만약 구간의 합이 k보다 더 작다면 계속 now의 값을 뒤로 이동시키고
만약 구간의 합이 k보다 더 크다면 구간에서 제일 앞에 있는 값이 빼줘야한다.
pre를 사용해서 구간의 앞에 수를 빼고 뒤로 이동시킨다.

만약 구간 합이 k와 같다면 answer에 저장한다.

답을 제출할 때는 answer에 있는 값 중에서 구간 길이가 가장 작고
앞에 있는 구간을 찾아서 답을 도출한다.

"""

def solution(sequence, k):
    answer = []
    len_seq = len(sequence)
    sum_num = 0
    pre = 0
    now = -1
    
    while True:
        if sum_num < k:
            now += 1
            if now >= len_seq:
                break
            sum_num += sequence[now]
        elif sum_num > k:
            sum_num -= sequence[pre]
            if pre >= len_seq:
                break
            pre += 1
        else:
            answer.append([pre, now])
    
    return answer