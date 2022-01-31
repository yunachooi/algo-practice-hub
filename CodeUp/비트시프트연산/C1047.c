#include <stdio.h>

int main(){
    int a;

    scanf("%d", &a);

    printf("%d", a << 1); // 오른쪽에 주어진 개수만큼 2베 곱하기
    printf("%d", a >> 1); // 오른쪽에 주어진 개수만큼 2배 나누기

    return 0;
}