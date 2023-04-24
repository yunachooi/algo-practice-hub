import math

cnt = 0
n = int(input())
num = str(math.factorial(n))

for i in num[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break
