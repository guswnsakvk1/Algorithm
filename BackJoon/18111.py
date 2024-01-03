"""
1. 0~256까지 for문을 돌린다. 
-> 높이 범위가 0~256이기 때문

2. 만약 현재 블럭의 높이가 target보다 높으면
   del_block에 현재 블럭 높이 - target 더하기

3. 만약 현재 블럭의 높이가 target보다 낮으면
   install_block에 target - 현재 블럭 높이 더하기

4. 만약 del_block - install_block + inven이 0보다 클 경우
1) num이라는 변수를 del_block * 2 + install_block 로 초기화
2) answer_time 보다 num이 작을 경우
   answer_time = time, answer_target = target
3) answer_time 이랑 num이 같을 경우
   answer_target = target
"""
import sys
input_fun = sys.stdin.readline

n, m, inven = map(int, input_fun().split())
answer_time = 1e9
answer_target = 0
ground = []

for i in range(n):
  ground.append(list(map(int, input_fun().split())))

for target in range(256, -1, -1):
  del_block = 0
  install_block = 0
  time = 0

  for i in range(n):
    for j in range(m):
      now_ground = ground[i][j]
      if now_ground > target:
        del_block += now_ground - target

      if now_ground < target:
        install_block += target - now_ground

  if del_block - install_block + inven >= 0:
    num = del_block * 2 + install_block
    if answer_time > num:
      answer_time = num
      answer_target = target

print(answer_time, answer_target)