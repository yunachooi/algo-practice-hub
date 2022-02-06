#include <stdio.h>
int main(){
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    printf("%d", (a < b ? a : b) < c ? (a < b ? a : b) : c); // 가장 작은 값 계산

    return 0;
}