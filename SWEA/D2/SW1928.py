encode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

T = int(input())

for test_case in range(1, T + 1) :
    N = input()
    length = len(N)
    tmp = ''
    
    for i in range(len(N)) :
        num = encode.index(N[i])
        bin_num = bin(num)[2:]
        
        while len(bin_num) < 6 :
            bin_num = '0' + bin_num
        tmp += bin_num

    answer = ''
    for i in range(length * 6 // 8) :
        c = int(tmp[i * 8 : i * 8 + 8], 2)
        answer += chr(c)
        
    print(f"#{test_case} {answer}")
