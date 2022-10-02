lst = [0] * 26
s = input()

for i in s:
    lst[ord(i) - 97] += 1   # 소문자 a = 97, z = 122

print(*lst)
