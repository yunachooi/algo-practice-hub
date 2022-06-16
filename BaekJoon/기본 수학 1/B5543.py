n = []

for i in range(5):
  n.append(int(input()))

h = min(n[0:3]) # 햄버거
d = min(n[3:5]) # 음료

set = h + d - 50
print(set)
