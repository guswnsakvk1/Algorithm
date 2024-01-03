n = input()
lst =  ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in lst:
  n = n.replace(change, "a")

print(len(n))