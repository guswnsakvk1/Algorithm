def recur(num, s, lst):
    if num == m:
        answer.append(lst)
        return
    
    for i in range(s, n+1):
        recur(num+1, i, lst+[i])

n, m = map(int, input().split())

answer = []
recur(0, 1, [])

for a in answer:
    print(' '.join(map(str, a)))