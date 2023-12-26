import sys
lst = sys.stdin.readlines()[1 : ]

lst.sort(key=lambda x : (int(x.split()[1]), int(x.split()[0])))  

print(''.join(lst))
