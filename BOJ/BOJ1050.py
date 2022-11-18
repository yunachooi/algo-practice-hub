N = list(input())
a, e, i, o, u = 0, 0, 0, 0, 0

for k in range(len(N)):
    if N[k] == 'a' or N[k] == 'A':
        a += 1
    elif N[k] == 'e' or N[k] == 'E':
        e += 1
    elif N[k] == 'i' or N[k] == 'I':
        i += 1
    elif N[k] == 'o' or N[k] == 'O':
        o += 1
    elif N[k] == 'u' or N[k] == 'U':
        u += 1
        
print(a)
print(e)
print(i)
print(o)
print(u)
