hour, minute = list(map(int, input().split()))

minute -= 45

if minute < 0:
  if hour == 0:
    hour = 23
  else:
    hour -= 1
  minute += 60

print(hour, minute)