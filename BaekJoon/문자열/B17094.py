n = int(input())
s = input()

a = s.count('2')
b = s.count('e')

print("yee" if a == b else (2 if a > b else "e"))
