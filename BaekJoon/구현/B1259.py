while True:
    a = input()
    b = 0
    if len(a) == 1 and a[0] == '0' :
        break

    for i in range(len(a)//2) :
        if a[i] != a[len(a)-1-i] :
            print("no")
            b = -1
            break

    if b == 0 :
        print("yes")
