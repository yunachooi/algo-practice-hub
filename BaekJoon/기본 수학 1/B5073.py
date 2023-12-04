while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
        
    sides = sorted([a, b, c])
    max_side = sides[2]
    sum_of_other_sides = sides[0] + sides[1]

    if max_side >= sum_of_other_sides:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
