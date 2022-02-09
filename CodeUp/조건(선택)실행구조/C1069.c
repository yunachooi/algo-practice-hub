#include <stdio.h>

int main() {
    char a;

    scanf("%c", &a);

    switch(a) { // 정수값만 가능
        case 'A': printf("best!!!"); break;
            //문자 'A'가 정수값 65('A'의 아스키 값)로 저장되기 때문에 가능
        case 'B': printf("good!!"); break;
        case 'C': printf("run!"); break;
        case 'D': printf("slowly~"); break;
        default: printf("what?");
    } // switch

    return 0;
}