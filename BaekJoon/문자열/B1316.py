N = int(input())
cnt = N

for _ in range(N):
    lst = input()
    for i in range(0, len(lst)-1):
        if lst[i] == lst[i + 1]:
            pass
        elif lst[i] in lst[i + 2:]:
            cnt -= 1
            break

print(cnt)
