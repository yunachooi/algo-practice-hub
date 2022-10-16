lst = [1] * 1001
cnt = 0

for i in range(10):
    n = int(input())
    lst[n] += 1
    cnt += n

print(int(cnt/10))  #avg
print(lst.index(max(lst)))  #max
