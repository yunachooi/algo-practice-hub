b = input()  # bowl
t = 10   # total

for i in range(1, len(b)):
    if b[i - 1] != b[i]:
        t += 10
    else:
        t += 5

print(t)
