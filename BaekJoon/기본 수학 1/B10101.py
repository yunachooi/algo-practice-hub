angles = []

for _ in range(3):
    angles.append(int(input()))
angles.sort()

if sum(angles) != 180:
    print("Error")

else:
    if angles[0] == angles[1]:
        if angles[1] == angles[2]:
            print("Equilateral")
        else:
            print("Isosceles")
    elif angles[1] == angles[2]:
        print("Isosceles")
    else:
        print("Scalene")
