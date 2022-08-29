cur = list(map(int, input().split(':')))
total = list(map(int, input().split(':')))

curtime = cur[0] * 3600 + cur[1] * 60 + cur[2]
totime = total[0] * 3600 + total[1] * 60 + total[2]

s = totime - curtime

if s < 0:
    s += 60 * 60 * 24
    
m = s // 60
s %= 60
h = m // 60
m %= 60

print("%02d:%02d:%02d" %(h, m, s))
