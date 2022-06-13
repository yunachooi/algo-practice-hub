n = list(map(int, input().split()))
result = 0

for i in n :
    result += i*i
result %=10

print(result)

         
