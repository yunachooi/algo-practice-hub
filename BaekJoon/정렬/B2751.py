from sys import stdin

case = int(stdin.readline().strip())

num_list = []

for i in range(case):
    num_list.append(int(stdin.readline().strip()))

num_list.sort()
for i in range(case):
    print(num_list[i])
