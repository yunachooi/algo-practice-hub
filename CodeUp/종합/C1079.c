#include <stdio.h>

int main(){
    char n;

    while(1){
        scanf("%c ", &n);

        printf("%c\n", n);
        if(n == 'q') // q가 입력될 때까지 실행
            break;
    }

    return 0;
}