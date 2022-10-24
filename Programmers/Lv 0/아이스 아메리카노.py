def solution(money):
    answer = []
    caffe = money // 5500
    rest = money % 5500
    answer = [caffe, rest]
    return answer
