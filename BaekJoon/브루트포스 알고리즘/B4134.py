import sys
input = sys.stdin.readline

def sosu(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,i nt(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(int(input())):
    x = int(input().rstrip())
    
    while True:
        if(sosu(x)):
            print(x)
            break
        x += 1
