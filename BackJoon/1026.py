## list_a[i]값과 list_b[i]값의 곱의 최소합을 구하려면
## 하나의 리스트를 오름차순, 하나의 리스트는 내림차순으로 정렬하고
## index번호가 같은 값을 곱하고 answer에 더해주면 된다

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse=True)

answer = 0

for i in range(n):
  answer += (list_a[i] * list_b[i])

print(answer)