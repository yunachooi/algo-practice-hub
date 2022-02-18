#include <stdio.h>

int main(){
    int n;
    scanf("%X", &n); // 16진수

    for(int i = 1; i <= 15; i++) // 1단부터 15단까지
        printf("%X*%X=%X\n", n, i, n * i);

    return 0;
}