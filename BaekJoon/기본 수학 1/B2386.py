import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '#':
        break

    alphabet = line[0]
    line = str.lower(line[2:])
    print(alphabet, line.count(alphabet))
