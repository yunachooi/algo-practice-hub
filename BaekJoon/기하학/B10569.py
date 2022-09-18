import sys
input = sys.stdin.readline  #시간 초과 방지

t = int(input())

for _ in range(t):
    v, e = map(int, input().split()) #꼭짓점, 모서리 개수
    
    f = 2 - (v - e) #면의 수
    
    print(f)
