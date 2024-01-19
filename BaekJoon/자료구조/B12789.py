from collections import deque

N = int(input())
Row = deque(map(int, input().split()))
Col = []


Order = 1
while True:
  if Row and Row[0] == Order:
    Row.popleft()
    Order += 1
    
  elif Col and Col[-1] == Order:
    Col.pop()
    Order += 1
    
  elif Row:
    Pop = Row.popleft()
    Col.append(Pop)
    
  else:
    break
  
if Row or Col:
  print("Sad")
  
else:
  print("Nice")
