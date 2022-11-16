T = int(input())

for test_case in range(1, T + 1):
    N = input()

    year = int(N[ : 4])
    month = int(N[4 : 6])
    day = int(N[6 : 8])
    day_dict = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31,
                6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31,
                11 : 30, 12 : 31}

    if month >= 13 or month <= 0 :
        print('#{} -1'.format(test_case))
        continue
    else:
        if day_dict[month] < day or day <= 0:
            print('#{} -1'.format(test_case))
            continue
        else:
            print('#%d %.4d/%.2d/%.2d' %(test_case, year, month, day))
    
