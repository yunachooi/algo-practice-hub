t = int(input())

for _ in range(t):
    n, m = map(int,input().strip().split())
    
    print(sum(str(i).count('0') for i in range(n, m + 1)))
