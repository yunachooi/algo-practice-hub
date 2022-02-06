#include <stdio.h>
int main(){
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d", a > b ? a : b); // "조건식 ? (참일 때의 값) : (거짓일 때의 값)” 의 형태

    return 0;
}