import sys
name_list = sys.stdin.readlines()[1:]

name_list.sort(key=lambda iD : int(iD.split()[0]))

print("".join(name_list))
