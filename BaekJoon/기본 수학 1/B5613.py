a = int(input())

while True:
        b = input()
        if b == '=':
            break

        c = int(input())
        if b == '+':
                a = a + c
        elif b == '-':
                a = a - c
        elif b == '*':
                a = a * c
        elif b == '/':
                a = a // c
print(a)
