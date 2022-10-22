stack = []

s = stack
s.append(5) # append = 삽입
s.append(2)
s.append(3)
s.append(7)
s.pop() # pop = 삭제
s.append(1)
s.append(4)
s.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
