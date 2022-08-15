while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:   # 종료
        break
    if b % a == 0:  # 첫 번째 숫자가 두 번째 숫자의 약수인 경우
        print('factor')

    elif a % b == 0:    # 배수인 경우
        print('multiple')

    else:   # 둘 다 아닌 경우
        print('neither')
        
