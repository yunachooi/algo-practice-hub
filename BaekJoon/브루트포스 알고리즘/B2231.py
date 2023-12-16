N = int(input())
trigger = False

start_case = max(0, N - 9 * len(str(N)))
for i in range(start_case, N):

    digits = [int(j) for j in str(i)]
    if sum(digits) + i == N:
        print(i)
        trigger = True
        break

if not trigger:
    print(0)
