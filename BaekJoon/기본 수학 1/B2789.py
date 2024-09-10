word = input().strip()
 
censor_word = "CAMBRIDGE"
 
result = ''.join(char for char in word if char not in censor_word)
print(result)
