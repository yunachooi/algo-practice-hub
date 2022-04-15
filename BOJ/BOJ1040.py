class Queue:

    def __init__(self):
        self.__list = []
        self.__front = 0

    def empty(self):
        return self.__front == len(self.__list)

    def enqueue(self, item):
        self.__list.append(item)

    def front(self):
        if not self.empty():
            return self.__list[self.__front]
        else:
            print('Error in front()')
            sys.exit()

    def dequeue (self): # front 원소 삭제 후 리턴
        if not self.empty():
            self.__front += 1
            return self.__list [self.__front-1]
        else:
            print('Error in dequeue()')
            sys.exit()
# end Queue


n = int(input())
car = [int (x) for x in input().split()]

Q = Queue()

num = 1
i = 0
while num <= n:
    if i < n and car[i] == num:
        num += 1
        i += 1
    elif not Q.empty() and Q.front() == num:
        Q.dequeue()
        num += 1
    elif i < n:
        Q.enqueue(car[i])
        i += 1
    else:
        break

if num < n:
    print('NO')
else:
    print('YES')
    



    
