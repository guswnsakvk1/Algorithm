"""
현재와 앞에 있는 기름값을 비교해서 더 싼 것을 넣는다.
만약 i가 len(gas_stations) - 1 과 같다면
현재 위치의 주유소에서 기름을 넣어야한다.
"""

n = int(input())
roads = list(map(int, input().split()))
gas_stations = list(map(int, input().split()))

answer = 0
now = 0

for i in range(1, n):
    if n == len(gas_stations) - 1:
        answer += gas_stations[now] * roads[i-1]
        break
    
    answer += gas_stations[now] * roads[i-1]
    
    if gas_stations[now] > gas_stations[i]:
        now = i

print(answer)