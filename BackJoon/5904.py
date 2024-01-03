N = int(input())

length = 3
n = 0

def moo(length, middle, N):
  pre = (length - middle) // 2
  if pre >= N:
    return moo(pre, middle - 1, N)
  elif pre + middle < N:
    return moo(pre, middle - 1, N - pre - middle)
  else:
    return "o" if N-pre-1 else "m"

while N > length:
  n += 1
  length = length * 2 + 3 + n

print(moo(length, n + 3, N))