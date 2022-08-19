t = int(input())

for _ in range(t):
    maxs, maxl = "", 0
    n = int(input())    # 학교 숫자
    
    for _ in range(n):
        s, l = map(str, input().split())    # 학교이름, 소비한 술의 양
        l = int(l)
        
        if l > maxl:
            maxl = l
            maxs = s

    print(maxs)
