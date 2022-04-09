class Stack:
    
    def __init__(self):
        self.__list = []
    def empty(self):
        return len(self.__list) == 0
    def push(self, item):
        self.__list.append(item)
    def top(self):
        return self.__list[-1]
    def pop(self):
        return self.__list.pop()
# end Stack


n = int(input())
A = [int(x) for x in input().split()]   # 리스트 생성

S = Stack()
O = []

S.push(A[n-1])  # 마지막 숫자
O.append(-1)

for i in range(n - 2, -1, -1):
    while not S.empty():
        if A[i] < S.top(): break
        S.pop()
    if S.empty(): O.append(-1)
    else: O.append(S.top())
    S.push(A[i])

O.reverse()
for x in O:
    print(x, end=" ")
    
