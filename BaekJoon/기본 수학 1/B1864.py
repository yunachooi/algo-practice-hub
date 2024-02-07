symbols = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']

while True:
    word = input()
    
    if word == '#': exit()
    else:
        tmp = len(word) - 1
        result = 0
        
        for i in word:
            if i == '/':
                result += -1 * (8 ** tmp); tmp -= 1
            else:
                result += symbols.index(i) * (8 ** tmp); tmp -= 1
        print(result)
