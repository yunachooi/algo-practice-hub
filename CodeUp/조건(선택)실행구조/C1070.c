#include <stdio.h>

int main() {
    int a;

    scanf("%d", &a);

    switch(a) {
        case 12:
        case 1:
        case 2:
            printf("winter"); break;
            // break;를 제거하면 멈추지 않고 다음 명령이 실행되는 특성을 이용
        case 3:
        case 4:
        case 5:
            printf("spring"); break;
        case 6:
        case 7:
        case 8:
            printf("summer"); break;
        case 9:
        case 10:
        case 11:
            printf("fall"); break;
    } // switch

    return 0;
}