n = input()

lst = [i for i in n]
lst.sort(reverse = True)

[print(i, end = '') for i in lst]
