lst = list(input())

for i in range(len(lst)):
    if lst[i].isalpha():
        cnt = ord(lst[i]) + 13
        
        if cnt > 122:
            cnt -= 122
            cnt += 96
        elif cnt > 90 and cnt < 110:
            cnt -= 90
            cnt += 64
        lst[i] = chr(cnt)

print(''.join(lst))
