Grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
Credit_Sum = 0
Grade_Sum = 0

for i in range(20):
    Subject = list(map(str, input().split()))
    
    if Subject[2] != 'P':
        Credit_Sum += float(Subject[1])
        Grade_Sum += (float(Subject[1]) * Grade[Subject[2]])

print(round(Grade_Sum/Credit_Sum, 6))
