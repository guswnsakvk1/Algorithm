import sys
input = sys.stdin.readline

def left_to_right():
  can_pass = 0
  tmp = [[0] * N for _ in range(N)]

  for i in range(N):
    for j in range(1, N):
      tmp[i][j] = road[i][j] - road[i][j-1]

  for i in range(N):
    is_pass = True
    set_road = [False] * N
    for j in range(N):
      if tmp[i][j] == 0:
        continue
      elif tmp[i][j] == 1:
        cnt = 0
        for k in range(j-1,-1,-1):
          if road[i][j] - road[i][k] == 1 and not set_road[k]:
            cnt += 1
          else:
            break

        if cnt < L:
          is_pass = False
        else:
          for k in range(j-1,j-1-L,-1):
            set_road[k] = True
      elif tmp[i][j] == -1:
        cnt = 0
        for k in range(j, N):
          if road[i][j-1] - road[i][k] == 1 and not set_road[k]:
            cnt += 1
          else:
            break

        if cnt < L:
          is_pass = False
        else:
          for k in range(j, j+L):
            set_road[k] = True
      else:
        is_pass = False
        break
    
    if is_pass:
      can_pass += 1

  return can_pass

def up_to_down():
  can_pass = 0
  tmp = [[0] * N for _ in range(N)]

  for i in range(N):
    for j in range(1, N):
      tmp[j][i] = road[j][i] - road[j-1][i]

  for i in range(N):
    is_pass = True
    set_road = [False] * N
    for j in range(N):
      if tmp[j][i] == 0:
        continue
      elif tmp[j][i] == 1:
        cnt = 0
        for k in range(j-1, -1, -1):
          if road[j][i] - road[k][i] == 1 and not set_road[k]:
            cnt += 1
          else:
            break

        if cnt < L:
          is_pass = False
        else:
          for k in range(j-1, j-1-L, -1):
            set_road[k] = True
      elif tmp[j][i] == -1:
        cnt = 0
        for k in range(j, N):
          if road[j-1][i] - road[k][i] == 1 and not set_road[k]:
            cnt += 1
          else:
            break

        if cnt < L:
          is_pass = False
        else:
          for k in range(j, j+L):
            set_road[k] = True
      else:
        is_pass = False
        break

    if is_pass:
      can_pass += 1
  
  return can_pass
               
N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
answer = 0

answer += left_to_right()
answer += up_to_down()

print(answer)