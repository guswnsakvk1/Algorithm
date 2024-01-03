def recur(num, lst):
    if num == m:
        answer.append(lst)
        return
    
    for i in range(1, n+1):
        recur(num+1, lst + [i])

n, m = map(int, input().split())

answer = []
recur(0, [])

for a in answer:
    print(' '.join(map(str, a)))