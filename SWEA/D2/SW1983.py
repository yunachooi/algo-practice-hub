T = int(input())

for test_case in range(1, T + 1):
    N, K = [int(x) for x in input().split()]
    students = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    for _ in range(N):
        M, F, H = [int(y) for y in input().split()]
        total = M * 0.35 + F * 0.45 + H * 0.20
        students.append(total)

    k_score = students[K - 1]
    students.sort(reverse=True)

    rank = students.index(k_score) // (N // 10)  # 핵심 코드
    k_grade = grade[rank]

    print(f'#{test_case} {k_grade}')
