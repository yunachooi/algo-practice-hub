N = list(input())

for i in range(len(N)):
    print(ord(N[i]) - 64, end = ' ')
    # ord = 단일 문자의 아스키 코드 값을 돌려주는 함수.
