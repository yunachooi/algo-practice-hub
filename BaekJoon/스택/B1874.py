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


def isOK():
    global O
    S = Stack()
    num = 1
    for i in range(n):
        while T[i] > num:
            S.push(num)
            num += 1
            O.append('+')
        if T[i] == num:
            O.append('+')
            O.append('-')
            num += 1
        elif not S.empty() and T[i] == S.top():
            S.pop()
            O.append('-')
        else:
            return False
    return True

# main program
n = int(input())
T = []
for i in range(n):
    T.append(int(input()))
O = []
if isOK():
    for x in O:
        print(x)
else:
    print('NO')
    
