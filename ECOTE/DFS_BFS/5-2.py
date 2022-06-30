from collections import deque

# 큐(queue) 구현을 위해 deque 라이브러리 사용
q = queue = deque()


q.append(5) # 삽입
q.append(2)
q.append(3)
q.append(7)
q.popleft() # 삭제
q.append(1)
q.append(4)
q.popleft()

print(queue)
q.reverse() # 역순
print(queue)
