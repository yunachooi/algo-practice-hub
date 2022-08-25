n = int(input())
v = [0 for _ in range(n)]   # list 초기화
# 참고 : [0] * n이 더 좋은 초기화 방법 

for i in range(n):
    v[i] = int(input())

for i in range(n):
    if v[0] != max(int(v[0]), int(v[i])):
        val = 'N'
        break;
    
    else:
        val = 'S'

print(val)
