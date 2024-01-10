# gcd 최소공배수
def get_gcd(a, b):
    a, b = (a, b) if a > b else (b, a)

    while b :
        a, b = b, a % b
        
    return a

# main
a, b= map(int, input().split())

gcd = get_gcd(a, b)

print(a * b // gcd)
