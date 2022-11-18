T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    M = [int(x) + N for x in input().split()][::-1]
    MAX, answer = M[0], 0
    
    for i in range(1, N):
        if MAX > M[i]:
            answer += MAX - M[i]
        else:
            MAX = M[i]

    print('#%d %d' %(test_case, answer))
