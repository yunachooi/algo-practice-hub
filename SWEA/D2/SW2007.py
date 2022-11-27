T = int(input())

for test_case in range(T):
    length = 0
    
    N = [x for x in input()]

    for i in range(1, len(N) + 1):
        if N[0] == N[i]:
            if N[1] == N[i + 1]:
                length = i
                break
        
    print('#{} {}'.format(test_case, length))
