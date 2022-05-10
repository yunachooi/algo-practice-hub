a, b, c = map(int, input().split()) # 시, 분, 초
d = int(input())                    # 필요시간(초)

a = (a + (b + (c + d) // 60) // 60) % 24  # // 정수부분 반환
b = (b + ((c + d) // 60)) % 60
c = (c + d) % 60

print(a, b, c)
