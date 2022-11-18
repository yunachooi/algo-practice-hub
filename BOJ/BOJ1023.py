K = int(input())    #분 당 사용료
A, B = map(int, input().split())
C, D = map(int, input().split())

if B > D:
    A += 1
    m = (60 - B) + D
else:
    m = D - B
    
if A > C:
    h = ((C + 24) - A) * 60
else:
    h = (C - A) * 60

print(K * (h + m))
