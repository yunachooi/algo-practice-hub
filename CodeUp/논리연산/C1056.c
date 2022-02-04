#include <stdio.h>

int main(){
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d", (a && !b) || (!a && b)); // 참 / 거짓이 서로 다를 때에만 1로 계산

    return 0;
}