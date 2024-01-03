"""
1. add x: S에 x를 추가한다. 
   (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.

2. remove x: S에서 x를 제거한다. 
   (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.

3. check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)

4. toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)

5. all: S를 {1, 2, ..., 20} 으로 바꾼다.

6. empty: S를 공집합으로 바꾼다. 
"""

import sys

input_func = sys.stdin.readline

num = int(input_func().rstrip())
s = set()

for i in range(num):
    cmds = input_func().rstrip()
    cmd = cmds.split()

    if len(cmd) > 1:
        num = int(cmd[1])
    kind = cmd[0]

    if kind == 'add':
        s.add(num)
    elif kind == 'remove':
        if num in s:
            s.remove(num)
    elif kind == 'check':
        print(1) if num in s else print(0)
    elif kind == 'toggle':
        s.remove(num) if num in s else s.add(num)
    elif kind == 'all':
        s.clear()
        s.update({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
    else:
        s.clear()