a,b = sorted(map(int,input().split())) # 정렬함수

if a == b:
   print(0)

else:
   print(b - a - 1)
   for i in range(a + 1, b):
      print(i, end=' ')
