from collections import deque
import sys
input = sys.stdin.readline

wheel = []
for _ in range(4):
    lst = list(map(int, input().rstrip()))
    wheel.append(deque(lst))

k = int(input())

for _ in range(k):
    n, turn = map(int, input().split())
    check1 = False
    check2 = False
    check3 = False

    if wheel[0][2] != wheel[1][6]:
        check1 = True

    if wheel[1][2] != wheel[2][6]:
        check2 = True

    if wheel[2][2] != wheel[3][6]:
        check3 = True

    if n == 1:
      if turn != 1:
        wheel[0].append(wheel[0].popleft())

        if check1:
            wheel[1].appendleft(wheel[1].pop())
        else:
            continue
            
        if check2:
            wheel[2].append(wheel[2].popleft())
        else:
            continue

        if check3:
            wheel[3].appendleft(wheel[3].pop())
        else:
            continue
      else:
        wheel[0].appendleft(wheel[0].pop())

        if check1:
            wheel[1].append(wheel[1].popleft())
        else:
            continue

        if check2:
            wheel[2].appendleft(wheel[2].pop())
        else:
          continue

        if check3:
            wheel[3].append(wheel[3].popleft())
        else:
            continue
    
    if n == 2:
        if turn != 1:
            wheel[1].append(wheel[1].popleft())

            if check1:
                wheel[0].appendleft(wheel[0].pop())

            if check2:
                wheel[2].appendleft(wheel[2].pop())
            else:
                continue
            
            if check3:
                wheel[3].append(wheel[3].popleft())
            else:
                continue
        else:
            wheel[1].appendleft(wheel[1].pop())

            if check1:
                wheel[0].append(wheel[0].popleft())

            if check2:
                wheel[2].append(wheel[2].popleft())
            else:
                continue
            
            if check3:
                wheel[3].appendleft(wheel[3].pop())
            else:
                continue

    if n == 3:
        if turn != 1:
            wheel[2].append(wheel[2].popleft())

            if check3:
                wheel[3].appendleft(wheel[3].pop())

            if check2:
                wheel[1].appendleft(wheel[1].pop())
            else:
                continue
            
            if check1:
                wheel[0].append(wheel[0].popleft())
            else:
                continue
        else:
            wheel[2].appendleft(wheel[2].pop())

            if check3:
                wheel[3].append(wheel[3].popleft())

            if check2:
                wheel[1].append(wheel[1].popleft())
            else:
                continue
            
            if check1:
                wheel[0].appendleft(wheel[0].pop())
            else:
                continue
    
    if n == 4:
        if turn != 1:
          wheel[3].append(wheel[3].popleft())

          if check3:
              wheel[2].appendleft(wheel[2].pop())
          else:
              continue
          
          if check2:
              wheel[1].append(wheel[1].popleft())
          else:
              continue
          
          if check1:
              wheel[0].appendleft(wheel[0].pop())
          else:
              continue
        else:
          wheel[3].appendleft(wheel[3].pop())

          if check3:
              wheel[2].append(wheel[2].popleft())
          else:
              continue
          
          if check2:
              wheel[1].appendleft(wheel[1].pop())
          else:
              continue
          
          if check1:
              wheel[0].append(wheel[0].popleft())
    

answer = 0
for i in range(4):
    if wheel[i][0] == 1:
        answer += 2 ** i

print(answer)