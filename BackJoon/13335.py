from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
bridge = deque([0] * w)
answer = 0
total = 0

trucks = deque(map(int, input().split()))
trucks.append(0)
truck = trucks.popleft()

while True:
  if total == 0 and not trucks:
    break
  
  answer += 1
  total -= bridge.popleft()

  if total + truck <= l:
    bridge.append(truck)
    total += truck
    if trucks:
      truck = trucks.popleft()
  else:
    bridge.append(0)

print(answer)