lst = input()
a, b = 0, 0 # 전부 0, 1로 바꾸는 경

if lst[0] == '1':
    a += 1
else:
    b += 1

for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:
        if lst[i + 1] == '1':
            a += 1
        else:
            b += 1

print(min(a, b))
