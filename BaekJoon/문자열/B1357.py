def rev(a):
    b = a[::-1]
    return int(b)

x, y = input().split()

resum = str(int(rev(x)) + int (rev(y)))
 
print(int(rev(resum)))
