t = int(input())

for _ in range(t):
    vowels = consonants = 0
    
    n = input().strip()
    n = n.replace(" ", "")
    
    for element in n:
        if element in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else :
            consonants += 1

    print(consonants, vowels)
