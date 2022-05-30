n = int(input())
no = cute = 0

for i in range (n):
    if int(input()) == 0:
        no += 1
    else:
        cute += 1

if no > cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
