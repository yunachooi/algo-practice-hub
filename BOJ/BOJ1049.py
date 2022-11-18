N = list(input().split(' '))
N2 = []

# 오름차순으로 정렬 후 '0' 삭제
N.sort()

delete = '0'
for i in N:
    if not delete in i:
        N2.append(i)
        
if not N2:  # 모두 0일 시 0 출력
    print(0, end = '')
else:     
    for i in range(len(N2)):
        print(N2[i], end = '')

# 줄 바꿈
print()

# 내림차순으로 정렬 
N.sort(reverse = True)
for i in range(len(N)):
    if N[0] == '0': # 모두 0일 시 0 출력
        print(0, end = '')
        break
    print(N[i], end = '')


# CASE2
'''
N = list(map(int, input().strip().split()))
N2 = []

N.sort()
N2 = N[0] * 10000 + N[1] * 1000 + N[2] * 100 + N[3] * 10 + N[4] * 1
N3 = N[4] * 10000 + N[3] * 1000 + N[2] * 100 + N[1] * 10 + N[0] * 1

print(N2)
print(N3)
'''
