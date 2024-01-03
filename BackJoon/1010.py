import math
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  west, east = map(int, input().split())

  print(int(math.factorial(east) / (math.factorial(east - west) * math.factorial(west))))