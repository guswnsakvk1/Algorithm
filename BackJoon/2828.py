import sys
input = sys.stdin.readline

N, M = map(int, input().split())
start = 1
end = M
answer = 0

J = int(input())

for _ in range(J):
  place = int(input())

  if start > place:
    num = start - place
    start -= num
    end -= num
    answer += num
  elif end < place:
    num = place - end
    start += num
    end += num
    answer += num

print(answer)