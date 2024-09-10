num = int(input())
q = input()

adrian = ['A','B','C']
bruno = ['B','A','B','C']
goran = ['C','C','A','A','B','B']

dic = [[0,'Adrian'],[0,'Bruno'],[0,'Goran']]

for i in range(len(q)):
    if adrian[i%len(adrian)] ==q[i]:
        dic[0][0]+=1

    if bruno[i%len(bruno)] ==q[i]:
        dic[1][0]+=1

    if goran[i%len(goran)] ==q[i]:
        dic[2][0]+=1

dic = sorted(dic,reverse=True,key=lambda x:x[0])

max_score = dic[0][0]
print(max_score)

for i in dic:
    if i[0]==max_score:
        print(i[1])
