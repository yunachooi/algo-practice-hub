from collections import deque
import sys
input = sys.stdin.readline

while True:
    char_list = deque()
    s = input().rstrip()
    
    if s == ".":
        break
        
    temp = True
    
    for i in s:
        if i == "(" or i == "[":
            char_list.append(i)
            
        elif(i == ")"):
            if(len(char_list) == 0 or char_list[-1] != "("):
                temp = False
                break
                
            else:
                char_list.pop()
                
        elif(i == "]"):
            if(len(char_list) == 0 or char_list[-1] != "["):
                temp = False
                break
                
            else:
                char_list.pop()
            
    print("yes" if temp and not char_list else "no")
