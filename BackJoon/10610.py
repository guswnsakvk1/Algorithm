"""
30의 배수는 각 자리 숫자들의 합이 3의 배수여야 한다.
-> 30의 배수는 각 자리 숫자들의 합이 3의 배수여야 하는 이유는 10과 3이 서로소이기 때문 
"""

n = list(input())
n.sort(reverse=True)

if n[-1] != '0':
    print(-1)
else:
    if sum(map(int, n)) % 3 == 0:
        print(int("".join(n)))
    else:
        print(-1)