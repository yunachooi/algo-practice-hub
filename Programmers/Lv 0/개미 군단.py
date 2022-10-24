def solution(hp):
    answer = 0
    ant_type = [5, 3, 1]
    for ant in ant_type:
        answer += hp // ant
        hp %= ant
    return answer
