## 모든 경우의 수를 구해서 비교해서 구하면 시간초과걸림
## 자리수를 사용해서 답을 구할 수 있음
## 예시, 입력: ABC, BCA
## ABC -> A * 100 + B * 10 + C * 1
## BCA -> B * 100 + C * 10 + A * 1
## ABC + BCA -> A * 101 + B * 110 + C * 11
## B = 9, A = 8, C = 7 대입하는 것이 가장 큰 수

n = int(input())

words = []
for i in range(n):
  words.append(input())

cnt = {}

for i in range(n):
  for j in range(len(words[i])):
    ## 만약 cnt['알파벳']이 있다면 (10 ** j) 더하기
    ## cnt['알파벳']이 없다면 (10 ** j)로 초기화 하기
    try:
      cnt[words[i][(-1 * (j + 1))]] += (10 ** j)
    except:
      cnt[words[i][(-1 * (j + 1))]] = (10 ** j)

## value가 높은 순으로 정렬하기
replace_str = sorted(cnt, key=lambda x:cnt[x], reverse=True)

## 입력받은 단어 숫자로 변경하기
for i in range(n):
  for j in range(len(replace_str)):
    words[i] = words[i].replace(replace_str[j], str(9-j))

print(sum(map(int, words)))