#include <stdio.h>

int main(){
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d", !(a || b)); // 모두 거짓일 때에만 참이 계산

    return 0;
}