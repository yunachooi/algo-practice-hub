m = int(input())
n = int(input())
lst = list()    #완전제곱수

i = 1
while i * i <= n:
    if m <= i * i <= n:
        lst.append(i * i)
    i += 1

if len(lst) == 0:
    print(-1)

else:
    print(sum(lst))
    print(min(lst))
