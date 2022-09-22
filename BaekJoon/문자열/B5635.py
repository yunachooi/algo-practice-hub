n = int(input())
student = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    student.append([name, int(dd), int(mm), int(yyyy)])
    
student.sort(key=lambda x:(-int(x[3]),-int(x[2]),-int(x[1])))
    #lambda 함수는 매개변수와 return 값을 지님.

print(student[0][0])    #가장 나이가 적은 사람
print(student[len(student)-1][0])   #가장 나이가 많은 사람
