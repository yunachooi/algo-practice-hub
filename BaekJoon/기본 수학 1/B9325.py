t = int(input())

for _ in range(t):
    s = int(input())    #자동차 가격
    n = int(input())    #옵션의 개수
    price = s
    
    for _ in range(n):
        q, p = map(int, input().split())    #특정 옵션 개수, 해당 옵션 가격

        price += q * p
        
    print(price)
