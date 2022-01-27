#include <stdio.h>

int main(){
    long long int a;

    scanf("%lld", &a);

    printf("%lld", ++a); // 변수를 사용하기 전에 증감을 먼저 수행

    return 0;
}