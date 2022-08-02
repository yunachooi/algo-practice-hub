n = int(input())

for _ in range(n):
    arr = input().strip().split()
    
    for _ in range(int(arr[0])):
        print(arr[1],end="")
        
    print()
