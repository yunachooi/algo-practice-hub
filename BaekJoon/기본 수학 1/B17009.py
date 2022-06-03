score = [int(input()) for _ in range(6)]

a = score[0] * 3 + score[1] * 2 + score[2] # Apples point
b = score[3] * 3 + score[4] * 2 + score[5] # Bananas point

if a == b:
    print('T')
elif a > b:
    print('A')
else:
    print('B')
