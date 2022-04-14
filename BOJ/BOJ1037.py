class Stack:
    
    def __init__(self):
        self.__list = []
        
    def empty(self):
        return len(self.__list) == 0
    
    def push(self, item):
        self.__list.append(item)
        
    def top(self):
        if not self.empty():
            return self.__list[-1]
        else:
            print('Error in top()')
            sys.exit()
        
    def pop(self):
        if not self.empty():
            return self.__list.pop()
        else:
            print('Error in pop()')
# end Stack


data = input()
S = Stack()

for ch in data:
    if ch.isdigit(): S.push(int(ch))
    else:
        if ch == ' ': continue
        y = S.pop()
        x = S.pop()
        if ch == '+': S.push(x+y)
        elif ch == '-': S.push(x-y)
        elif ch == '*': S.push(x*y)
        elif ch == '/': S.push(int(x/y))
        
print(S.top())
