import sys
n = sys.stdin.read()
word = [0]*26

for i in n:
    if i.islower():
        word[ord(i)-97] += 1
        
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end="")
