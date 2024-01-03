# for문 사용
lenght = int(input())
number = input()
total = 0
for i in range(lenght):
  total += int(number[i])

print(total)

# map 사용
n = input()
print(sum(list(map(int,input()))))