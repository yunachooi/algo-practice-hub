while True:
    arr = [0] * 26
    text = input()
    
    if text == "*": break
    flag = False
    for element in text:
        if element.isalpha(): arr[ord(element) - 97] += 1
            
    for i in range(26):
        if arr[i] == 0:
            flag = True; break
    print("N" if flag else "Y")
