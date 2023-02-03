n = input()
m = int(input())
tmp = int(n[: -2] + '00')

while True:
    if tmp % m == 0:
        break
    tmp += 1
print(str(tmp)[-2 :])
