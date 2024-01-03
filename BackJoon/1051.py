"""
결과 :  직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형의 크기

3x5 크기 직사각형이 있을 경우
1. 현재 사각형에서 구할 수 있는 가장 긴 정사각형의 변 길이 구하기
2. 2x2 정사각형부터 시작해서 3x3 정사각형까지 모든 정사각형을 구하기
3. 구한 정사각형의 꼭짓점을 확인

2x2 크기 정사각형 확인하는 과정
(0,0), (0,1), (1,0), (1,1) -> 배열에 저장해서 꼭짓점 확인
(0,1), (0,2), (1,1), (1,2) -> 배열에 저장해서 꼭짓점 확인
"""

def check(new_rectangle, num, answer):
  if new_rectangle[0][0] == new_rectangle[0][-1] == new_rectangle[-1][0] == new_rectangle[-1][-1]:
    return num
  else:
    return answer

answer = 1
n, m = map(int, input().split())

max_len = min(n, m)

rectangle = []
for _ in range(n):
  rectangle.append(list(input()))

for num in range(1, max_len):
  for i in range(n-num):
    for j in range(m-num):
      new_rectangle = []
      for k in range(num+1):
        new_rectangle.append(rectangle[i+k][j:j+num+1])
      answer = check(new_rectangle, num+1,answer)

print(answer ** 2)