answer = []
for i in range (8):
    answer.append(int(input()))

result = sorted(answer, reverse = True)
result_idx = []

for i in result[ : 5]:
    result_idx.append(answer.index(i) + 1)

print(sum(result[ : 5]))
result_idx.sort()
print(*result_idx)
