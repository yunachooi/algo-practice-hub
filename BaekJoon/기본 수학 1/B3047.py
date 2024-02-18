A, B, C = sorted(map(int, input().split()))
z = []

seq = input()
for i in seq:
  if i == "A":
    z.append(A)
  elif i == "B":
    z.append(B)
  else:
    z.append(C)

print(' '.join(map(str,z)))
