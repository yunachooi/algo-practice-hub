t = int(input())

for __ in range (t):
    n = bin(int(input())) # 2진수

    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')
            
