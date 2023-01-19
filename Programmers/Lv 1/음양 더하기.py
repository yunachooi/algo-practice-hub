def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else:
            answer.append(-1 * absolutes[i])
    return sum(answer)
