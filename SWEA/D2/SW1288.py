T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0
    
    graph = [str(i) for i in range(10)]
    while graph:
        cnt += 1
        room = N * cnt
        room = str(room)

        for i in room:
            if i in graph:
                graph.remove(i)
        
    print('#{} {}'.format(test_case, room))
    
