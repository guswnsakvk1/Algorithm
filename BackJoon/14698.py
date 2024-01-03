import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)

    answer = 1
    while len(slimes) != 1:
        slime_one = heapq.heappop(slimes)
        slime_two = heapq.heappop(slimes)
        energy = slime_one * slime_two
        heapq.heappush(slimes, energy)
        answer *= energy

    print(answer % 1000000007)