n = int(input())

while True:
    m = int(input())
    if m == 0:
        break
    print(("{} is NOT ".format(m) if m%n!=0 else "{} is ".format(m))+"a multiple of {}.".format(n))
