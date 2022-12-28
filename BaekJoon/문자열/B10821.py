s = list(input())
cnt = 0

for i in range(len(s)):
    if s[i] == ',':
        cnt += 1

print(cnt + 1)
